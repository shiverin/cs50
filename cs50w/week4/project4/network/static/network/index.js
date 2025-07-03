function startEdit(postId) {
    const postBodyDiv = document.getElementById(`post-body-${postId}`);
    document.getElementById(`bigpost-${postId}`).classList.add('editing');
    const content = postBodyDiv.querySelector('.post-content').innerText;

    postBodyDiv.querySelector('.post-content').innerHTML = `
    <textarea class="form-control" id="edit-textarea-${postId}" rows="1">${content}</textarea>
    <button class="btn btn-sm btn-primary mt-1" onclick="submitEdit(${postId})">Save</button>
    <button class="btn btn-sm btn-secondary mt-1 ms-1" onclick="cancelEdit(${postId}, '${content}')">Cancel</button>
  `;
}

function cancelEdit(postId, originalContent) {
    document.getElementById(`bigpost-${postId}`).classList.remove('editing');
    const postBodyDiv = document.getElementById(`post-body-${postId}`);
    postBodyDiv.querySelector('.post-content').innerHTML = originalContent;
}

function submitEdit(postId) {
    const newBody = document.getElementById(`edit-textarea-${postId}`).value;

    fetch(`/${postId}/edit/`, {
            method: 'PUT',
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                body: newBody
            }),
        })
        .then(response => {
            if (!response.ok) throw new Error("Edit failed");
            return response.json();
        })
        .then(data => {
            document.getElementById(`bigpost-${postId}`).classList.remove('editing');
            const postBodyDiv = document.getElementById(`post-body-${postId}`);
            postBodyDiv.querySelector('.post-content').innerHTML = data.new_body;
        })
        .catch(error => {
            alert("Failed to update post.");
            console.error(error);
        });
}

function likePost(postId) {
    const heart = document.querySelector(`.heart[onclick="likePost(${postId})"]`);
    const likeCount = heart.nextElementSibling;

    fetch(`/${postId}/like/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
                'Content-Type': 'application/json',
            },
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
                return;
            }

            if (data.liked) {
                heart.style.color = 'red';
                heart.style.webkitTextStroke = 'initial';
                heart.style.color = 'red';
                heart.textContent = '♥';
            } else {
                heart.style.color = 'transparent';
                heart.style.webkitTextStroke = '1px black';
                heart.textContent = '♥';
            }

            likeCount.textContent = data.likes_count;
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

function startFollow(username) {
    fetch(`/profile/${username}/follow/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
                'Content-Type': 'application/json',
            },
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
                return;
            }

            const btn = document.getElementById('follow-btn');
            const count = document.getElementById('follower-count');

            if (data.is_following) {
                btn.textContent = 'Unfollow';
                btn.classList.remove('btn-outline-primary');
                btn.classList.add('btn-outline-danger');
            } else {
                btn.textContent = 'Follow';
                btn.classList.remove('btn-outline-danger');
                btn.classList.add('btn-outline-primary');
            }

            count.textContent = data.follower_count;
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

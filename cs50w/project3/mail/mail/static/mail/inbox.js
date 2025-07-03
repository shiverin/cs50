document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);
  document.querySelector('#compose-form').addEventListener('submit', function(event) {
    event.preventDefault();
    send_email();
  });
  // By default, load the inbox
  load_mailbox('inbox');
});


function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
}

function load_mailbox(mailbox) {

  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;
  fetch(`/emails/${mailbox}`)
  .then(response => response.json())
  .then(emails => {
      // Print emails
      console.log(emails);

      // ... do something else with emails ...
      emails.forEach((email)=>{
        const inmail = document.createElement('div');
        inmail.className = 'email-entry';
        let sender=email["sender"];
        let subject=email["subject"];
        let time=email["timestamp"];
        let emailid=email["id"];
        let readed=email["read"];
        inmail.innerHTML = `
        <div class="email-left">
          <strong>${sender}</strong> ${subject}
        </div>
        <div class="email-right">
          ${time}
        </div>
        `;
        const emailRight = inmail.querySelector('.email-right');
        if (readed && mailbox!=="sent"){
          inmail.style.backgroundColor = "grey";
          emailRight.style.setProperty('color', 'white', 'important');
        }
        inmail.addEventListener('click', () => {
          read(emailid);
          view_email(emailid,mailbox);
        });
        document.querySelector('#emails-view').append(inmail);
    });
  });
}

function send_email(){
  console.log("send_email called");
  let recipients_input = document.querySelector('#compose-recipients');
  let recipients = recipients_input.value;
  let subject_input = document.querySelector('#compose-subject');
  let subject = subject_input.value;
  let body_input = document.querySelector('#compose-body');
  let body = body_input.value;
  fetch('/emails', {
    method: 'POST',
    body: JSON.stringify({
        recipients: recipients,
        subject: subject,
        body: body,
    })
  })
  .then(response => response.json())
  .then(result => {
      // Print result
      console.log(result);
      load_mailbox('sent')
  });
}

function view_email(id,mail){
  document.querySelector('#emails-view').innerHTML = '';
  fetch(`/emails/${id}`)
  .then(response => response.json())
  .then(email => {
      // Print email
      console.log(email);
      // ... do something else with email ...
      const viewmail = document.createElement('div');
      viewmail.className = 'email-view';
      let sender=email["sender"];
      let subject=email["subject"];
      let time=email["timestamp"];
      let recipients=email["recipients"];
      let emailid=email["id"];
      let body=email["body"];
      let arcstate=email["archived"];
      let butdiv = document.createElement('div');
      const buttonId = arcstate ? 'noarch' : 'yesarch';
      const buttonText = arcstate ? 'Unarchive this?' : 'Archive this?';
      let boolie = !(mail==="sent");
      viewmail.innerHTML = `
        <div class="view-first">
          <div>
            <strong>From:</strong> ${sender}
          </div>
          <div>
            ${
              boolie
                ? `<button class="btn btn-sm btn-outline-primary" id="${buttonId}">${buttonText}</button>`
                : ''
            }
          </div>
        </div>
        <div>
          <strong>To:</strong> ${recipients}
        </div>
        <div>
          <strong>Subject:</strong> ${subject}
        </div>
        <div>
          <strong>Timestamp:</strong> ${time}
        </div>
        <button class="btn btn-sm btn-outline-primary" id="reply">Reply</button>
        <hr>
        <div>
          ${body}
        </div>
      `;
      if (boolie){
        viewmail.querySelector(`#${buttonId}`).addEventListener('click', () => archive(emailid,arcstate));
      }
      viewmail.querySelector('#reply').addEventListener('click', ()=>reply(recipients, subject, body, time, sender));
      document.querySelector('#emails-view').append(viewmail);
  });
}

function reply(recipients,subject,body,time,sender){
  if (!subject.startsWith("Re: ")){
    subject="Re: "+subject;
  }
  body=`\"On ${time} ${sender} wrote: `+body+'\"';

  compose_email();
  document.querySelector('#compose-recipients').value = recipients;
  document.querySelector('#compose-subject').value = subject;
  document.querySelector('#compose-body').value = body;
}

function archive(id,bool){
  newstate=!bool;
  fetch(`/emails/${id}`, {
    method: 'PUT',
    body: JSON.stringify({
        archived: newstate
    })
  })
  .then(()=>load_mailbox('inbox'));
}

function read(idr){
  fetch(`/emails/${idr}`, {
    method: 'PUT',
    body: JSON.stringify({
        read: true
    })
  })
}

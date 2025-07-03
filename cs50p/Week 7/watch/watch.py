import re
import sys


def main():
    y = (input("HTML: "))
    a = y
    print(parse(a))


def parse(s):
    match = re.search("^<iframe.*src=\"https*://.*youtube\.com/embed/([a-zA-Z0-9_-]+)", s)
    if not match:
        return None
    else:
        x = match.group(1)
        return f"https://youtu.be/{x}"


if __name__ == "__main__":
    main()
# <iframe width="560" height="315" src="https://www.youtube.com/embed/xjh-g4WYo58?si=VgnrA6PpMhDkI4Cr" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

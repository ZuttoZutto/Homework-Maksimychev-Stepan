def wrap_html(text, tag):
    valid_tags = {
        "a", "abbr", "b", "body", "caption", "cite", "code", "div",
        "form", "h1", "h2", "h3", "h4", "h5", "h6", "header", "i", "s"
    }
    if tag not in valid_tags:
        print("Введён неверный тег")
    print(f"<{tag}>{text}</{tag}>")


s1, s2 = input(), input()
wrap_html(s1, s2)

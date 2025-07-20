# **Markdown** 💬

Markdown is a lightweight markup language that you can use to add formatting elements to plaintext text documents. Created by John Gruber in 2004, Markdown is now one of the world’s most popular markup languages.

Using Markdown is different than using a WYSIWYG editor. In an application like Microsoft Word, you click buttons to format words and phrases, and the changes are visible immediately. Markdown isn’t like that. When you create a Markdown-formatted file, you add Markdown syntax to the text to indicate which words and phrases should look different.

## **Bolding**

this is a **bold text**

## **Italic**

this is an *italicized text*

## **Blockquote**

> blockquote

## **Ordered List**

For ordered lists, use numbers followed by a period for the items like so 1.. Tabs still work for sub ordered lists.

1. First item
2. Second item
3. Third item

## **Unordered List**

For unordered lists use a hyphen - or asterisk '*' with a space before the text. If you want a sub bullet add a tab before the hyphen - or asterisk '*'.

- First item
- Second item
- Third item

## **Inputting LaTeX**

In the markdown cell, you can add LaTeX code between $ for inline outputs. You can also use two $$ to create its own cantered paragraph in display mode.

$ x = 2 $

- To add a little spacing in display mode, use \
- To add a new line when in math display mode, use \\
- To display a fraction, use \frac{arg 1}{arg 2}
- For power (superscripts text), use ^{}
- For indices (subscripts), use _{}
- For roots, use \sqrt[n]{arg}
- The [n] is optional.

## **Code**

`code`

## **Horizontal Rule**

---

## **Link**

[Markdown Guide](https://www.markdownguide.org)

## **Image**

![alt text](https://www.markdownguide.org/assets/images/tux.png)

## **Table**

| Syntax | Description |
| ----------- | ----------- |
| Header | Title |
| Paragraph | Text |

## **Fenced Code Block**

```python
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}

def func_test(parm1, parm2):
  return parm1
```

## **Strikethrough**

~~The world is flat.~~

## **Task List**

- [x] Write the press release
- [ ] Update the website
- [ ] Contact the media

## **Emoji**

(<https://github.com/ikatyang/emoji-cheat-sheet>)

(See also [Copying and Pasting Emoji](https://www.markdownguide.org/extended-syntax/#copying-and-pasting-emoji))

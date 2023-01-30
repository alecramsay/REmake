# Characters

There are a variety of character predicates for matching specific characters:

- character literals
- character classes
- character shorthands
- any character
- non-printable characters
- metacharacters, and
- special characters

All except the character shorthands `word_boundary` and `not_word_boundary` represent *consuming* characters 
and can be [quantified](quantifiers.md)).

## Character Literals

To match a specific character, simply double quote it.
For example, the pattern `"f"` matchines the letter 'f'.
Character patterns represented this way are restricted to the printable characters.

As a convenience, multi-character strings may also be represented as strings, e.g., `"foo"`
is equivalent to this:

```
"f" 
"o" 
"o"
```

## Character Classes

To match one of many possible characters, you can specify a character class as a series characters and/or ranges of characters:

<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" class="railroad-diagram" width="672.5" height="126" viewBox="0 0 672.5 126">
  <g transform="translate(.5 .5)">
    <g>
      <path d="M20 53v20m0 -10h20"></path>
    </g>
    <path d="M40 63h10"></path>
    <g class="terminal ">
      <path d="M50 63h0"></path>
      <path d="M95.5 63h0"></path>
      <rect x="50" y="52" width="45.5" height="22" rx="10" ry="10"></rect>
      <text x="72.75" y="67">any</text>
    </g>
    <path d="M95.5 63h10"></path>
    <path d="M105.5 63h10"></path>
    <g class="terminal ">
      <path d="M115.5 63h0"></path>
      <path d="M144 63h0"></path>
      <rect x="115.5" y="52" width="28.5" height="22" rx="10" ry="10"></rect>
      <text x="129.75" y="67">(</text>
    </g>
    <path d="M144 63h10"></path>
    <g>
      <path d="M154 63h0"></path>
      <path d="M247.5 63h0"></path>
      <path d="M154 63a12 12 0 0 0 12 -12v0a12 12 0 0 1 12 -12"></path>
      <g>
        <path d="M178 39h45.5"></path>
      </g>
      <path d="M223.5 39a12 12 0 0 1 12 12v0a12 12 0 0 0 12 12"></path>
      <path d="M154 63h24"></path>
      <g class="terminal ">
        <path d="M178 63h0"></path>
        <path d="M223.5 63h0"></path>
        <rect x="178" y="52" width="45.5" height="22" rx="10" ry="10"></rect>
        <text x="200.75" y="67">not</text>
      </g>
      <path d="M223.5 63h24"></path>
    </g>
    <path d="M247.5 63h10"></path>
    <g>
      <path d="M257.5 63h0"></path>
      <path d="M574 63h0"></path>
      <path d="M257.5 63h12"></path>
      <g>
        <path d="M269.5 63h0"></path>
        <path d="M562 63h0"></path>
        <path d="M269.5 63a12 12 0 0 0 12 -12v-8a12 12 0 0 1 12 -12"></path>
        <g class="terminal ">
          <path d="M293.5 31h78.25"></path>
          <path d="M459.75 31h78.25"></path>
          <rect x="371.75" y="20" width="88" height="22" rx="10" ry="10"></rect>
          <text x="415.75" y="35">"{char}"</text>
        </g>
        <path d="M538 31a12 12 0 0 1 12 12v8a12 12 0 0 0 12 12"></path>
        <path d="M269.5 63h24"></path>
        <g>
          <path d="M293.5 63h0"></path>
          <path d="M538 63h0"></path>
          <g class="terminal ">
            <path d="M293.5 63h0"></path>
            <path d="M381.5 63h0"></path>
            <rect x="293.5" y="52" width="88" height="22" rx="10" ry="10"></rect>
            <text x="337.5" y="67">"{char}"</text>
          </g>
          <path d="M381.5 63h10"></path>
          <path d="M391.5 63h10"></path>
          <g class="terminal ">
            <path d="M401.5 63h0"></path>
            <path d="M430 63h0"></path>
            <rect x="401.5" y="52" width="28.5" height="22" rx="10" ry="10"></rect>
            <text x="415.75" y="67">-</text>
          </g>
          <path d="M430 63h10"></path>
          <path d="M440 63h10"></path>
          <g class="terminal ">
            <path d="M450 63h0"></path>
            <path d="M538 63h0"></path>
            <rect x="450" y="52" width="88" height="22" rx="10" ry="10"></rect>
            <text x="494" y="67">"{char}"</text>
          </g>
        </g>
        <path d="M538 63h24"></path>
      </g>
      <path d="M562 63h12"></path>
      <path d="M269.5 63a12 12 0 0 0 -12 12v8a12 12 0 0 0 12 12"></path>
      <g class="terminal ">
        <path d="M269.5 95h132"></path>
        <path d="M430 95h132"></path>
        <rect x="401.5" y="84" width="28.5" height="22" rx="10" ry="10"></rect>
        <text x="415.75" y="99">|</text>
      </g>
      <path d="M562 95a12 12 0 0 0 12 -12v-8a12 12 0 0 0 -12 -12"></path>
    </g>
    <path d="M574 63h10"></path>
    <path d="M584 63h10"></path>
    <g class="terminal ">
      <path d="M594 63h0"></path>
      <path d="M622.5 63h0"></path>
      <rect x="594" y="52" width="28.5" height="22" rx="10" ry="10"></rect>
      <text x="608.25" y="67">)</text>
    </g>
    <path d="M622.5 63h10"></path>
    <path d="M 632.5 63 h 20 m 0 -10 v 20"></path>
  </g>
  <style>
    svg.railroad-diagram {
      background-color: #f5f5f5;
    }
    svg.railroad-diagram path {
      stroke-width: 3;
      stroke: black;
      fill: rgba(0, 0, 0, 0);
    }
    svg.railroad-diagram text {
      font: bold 14px monospace;
      text-anchor: middle;
      white-space: pre;
    }
    svg.railroad-diagram text.diagram-text {
      font-size: 12px;
    }
    svg.railroad-diagram text.diagram-arrow {
      font-size: 16px;
    }
    svg.railroad-diagram text.label {
      text-anchor: start;
    }
    svg.railroad-diagram text.comment {
      font: bold 12px monospace;
      fill: Orchid;
    }
    svg.railroad-diagram rect {
      stroke-width: 3;
      stroke: black;
      fill: PaleGreen;
    }
    svg.railroad-diagram rect.group-box {
      stroke: Plum;
      stroke-dasharray: 10 5;
      fill: none;
    }
    svg.railroad-diagram path.diagram-text {
      stroke-width: 3;
      stroke: black;
      fill: white;
      cursor: help;
    }
    svg.railroad-diagram g.diagram-text:hover path.diagram-text {
      fill: #eee;
    }
    svg.railroad-diagram g.optional-path rect {
      fill: PaleTurquoise;
    }
    
    @media (prefers-color-scheme: dark) {
      .day.dark-scheme {
        background: #333;
        color: white;
      }
      .night.dark-scheme {
        background: black;
        color: #ddd;
      }
    }
    
    @media (prefers-color-scheme: light) {
      svg.railroad-diagram {
        background-color: #f5f5f5;
      }
      svg.railroad-diagram path {
        stroke: black;
        fill: rgba(0, 0, 0, 0);
      }
      svg.railroad-diagram text.comment {
        fill: Orchid;
      }
      svg.railroad-diagram rect {
        stroke: black;
        fill: PaleGreen;
      }
      svg.railroad-diagram rect.group-box {
        stroke: Plum;
      }
      svg.railroad-diagram path.diagram-text {
        stroke: black;
        fill: white;
      }
      svg.railroad-diagram g.diagram-text:hover path.diagram-text {
        fill: #eee;
      }
      svg.railroad-diagram g.optional-path rect {
        fill: PaleTurquoise;
      }
    }
    
    @media (prefers-color-scheme: dark) {
      svg.railroad-diagram {
        background-color: #21222c;
      }
      svg.railroad-diagram path {
        stroke: silver;
        fill: rgba(0, 0, 0, 0);
      }
      svg.railroad-diagram text {
        fill: whitesmoke;
      }
      svg.railroad-diagram text.comment {
        fill: Orchid;
      }
      svg.railroad-diagram rect {
        stroke: silver;
        fill: DarkGreen;
      }
      svg.railroad-diagram rect.group-box {
        stroke: Plum;
      }
      svg.railroad-diagram path.diagram-text {
        stroke: silver;
        fill: darkslategrey;
      }
      svg.railroad-diagram g.diagram-text:hover path.diagram-text {
        fill: dimgray;
      }
      svg.railroad-diagram g.optional-path rect {
        fill: RoyalBlue;
      }
    }
  </style>
</svg>

For example, this represents any lower or upper case letter A through Z:

```
any ('a' - 'z' | 'A' - 'Z')
```

If you want the class to *exclude* characters, use the 'not' option.

## Character Shorthands

These are four pairs of predicates for regex character shorthands, 
shown along with their default translations (in Python):

| Word | Translation |
|------|-------------|
| digit() | \\d |
| not_digit() | \\D |
| word_character() | \\w |
| not_word_character() | \\W |
| whitespace() | \\s |
| not_whitespace() | \\S |
| word_boundary() | \\b |
| not_word_boundary() | \\B |

As mentioned above, `word_boundary` and `not_word_boundary` are non-consuming patterns and cannot be quantified.

## Any Character

This predicate matches any character except the newline:

| Word | Translation |
|------|-------------|
| any_character() | . |

To make this match the newline character, turn on the `dot_all` [inline mode modifier](modes.md)).

## Non-printable Characters

These predicates match non-printable characters:

| Word | Translation |
|------|-------------|
| bell() | \\a |
| escape() | \\e |
| form_feed() | \\f |
| newline() | \\n |
| carriage_return() | \\r |
| horizontal_tab() | \\t |
| vertical_tab() | \\v |

## Metacharacters

These predicates match the regex metacharacters:

| Word | Translation |
|------|-------------|
| dollar_sign() | \\$ |
| left_paren() | \\( |
| right_paren() | \\) |
| asterisk() | \\* |
| plus_sign() | \\+ |
| period() | \\. |
| question_mark() | \\? |
| left_bracket() | \\[ |
| right_bracket() | \\] |
| caret() | \\^ |
| left_brace() | \\{ |
| right_brace() | \\} |
| pipe() | \\\\| |

The translation escapes the metacharacter with a backslash.

## Special Characters

Finally, because character literals are quoted and [comments](comments.md) start with the hash symbol, 
use these predicates to match those characters:[^1]

| Word | Translation |
|------|-------------|
| single_quote() | ' |
| double_quote() | " |
| hash() | # |

For example, to match the quoted characters 'f', 'o', and 'o', do this:

```
double_quote()
"foo"
double_quote()
```

## Footnotes

[^1]: The hash symbol is also known as the number sign and pound sign.
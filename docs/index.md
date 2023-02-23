REmake implements a simple high-level language for authoring regular expressions. 
If regular expressions are like machine code, then the language is like assembler. 
You still deal with the low-level regex model, but you do it using more human-friendly terms.

The purpose of the language is to make it easier to write regular expressions for most *scenarios*,
as opposed to writing all regular expressions. In other words, there are some regex constructs & expressions that
you cannot generate using this tool, but you can create most of the regular expressions that you
probably care about using a much more readable and intentionally transparent language.

## Contents

These are the major language constructs:

- [Programs](programs.md)
- [Anchors](anchors.md)
- [Characters](characters.md)
- [Quantifiers](quantifiers.md)
- [Alternatives](alternatives.md)
- [Groups](groups.md)
- [Lookarounds](lookarounds.md)
- [Modes](modes.md)
- [Comments](comments.md)
- [Reserved Words](reserved.md)

## Overview

Regular expressions are left-to-right horizontal strings of characters.
This language allows you define top-to-bottom vertical sequences of predicates that must all match.
This sequence looks and feels much more like a traditional program.

Most predicates look like function calls, e.g., `digit()`.
A few look more like programming language constructs, e.g., `group( ... )`.
This is an example for finding floating pointing numbers:

```
digit() * 0, ...
period()
digit() * 1, ...
group (
  "e"
  digit() * 1, ...
) * 0, 1
```

When interpreted by the tool, this source produces a single-line regex: 

```
\d*\.\d+(?:e\d+)?
```

as well as a free-spaced regex:

```
\d                  # A digit
*                   # Zero or more times (greedy)
\.                  # A period (escaped)
\d                  # A digit
+                   # One or more times (greedy)
(?:                 # Begin group (not captured):
  e                 # The character 'e'
  \d                # A digit
  +                 # One or more times (greedy)
  )                 # End of group
?                   # Optionally (greedy)
```

You can find a library of examples in the examples directory in the GitHub [REmake repository](https://github.com/alecramsay/REmake).
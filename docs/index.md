REmake implements a simple high-level language for authoring regular expressions. 
If regular expressions are machine code, then the language is assembler. 
You still deal with the low-level regex model, but you do it using more human-friendly terms.

The purpose of the language is to make it easier to write regular expressions for most *scenarios*,
as opposed to writing all regular expressions. In other words, there are some regular expressions that
you cannot generate using this tool, but you can create most of the regular expressions that you
probably care about using a much more readable and intentionally transparent language.

## Contents

- [Overview](#overview)
- [Anchors](anchors.md)
- [Characters](characters.md)
- [Quantifiers](quantifiers.md)
- [Groups](groups.md)
- [Lookarounds](lookarounds.md)
- [Modes](modes.md)
- [Comments](comments.md)
- [Reserved Words](reserved.md)

## Overview

Regular expressions are left-to-right horizontal strings of characters.
This language allows you define top-to-bottom vertical sequences of predicates that must all match.
This sequence looks and feels much more like a program.

Most predicates look like function calls, e.g., `digit()`.
A few look more like programming language constructs, e.g., `all( ... )`.
Here's a simple example for finding floating pointing numbers:

```
digit() * 0, ...
period()
digit() * 1, ...
all (
  "e"
  digit() * 1, ...
) * 0, 1
```

Each of the major constructs in the language are enumerated in the [Table of Contents](#contents) above.
Here is a [library of examples](../examples/).
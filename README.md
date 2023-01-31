# REmake
A high-level language for building regular expressions (RE)

The purpose of the language is to make it easier to write regular expressions for most *scenarios*,
as opposed to writing most regular expressions.

## Installation

On macOS, download the UNIX executable REmake from the scripts/ directory, and
make sure it is in your PATH.

## Usage

```
REmake sample.re
```

For command documentation, type:

```
REmake -h
```

For example, this program for finding floating pointing numbers:

```
digit() * 0, ...
period()
digit() * 1, ...
all (
  "e"
  digit() * 1, ...
) * 0, 1
```

produces a single-line regex: 

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

## Documentation

The language is documented [here](https://alecramsay.github.io/REmake/).

## Feedback

I welcome your feedback:

- What language features would make this tool most useful?
- What output flavors would make this tool most useful?
- What operating systems would you like to see this tool support?
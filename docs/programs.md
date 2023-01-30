# Programs

Programs consist of a series of patterns that act like predicates that specify matches.
Each predicate has an implicit `matches a ...` before it, e.g., `matches a digit()`.

A program consists of an optional start anchor pattern, one or more non-anchor patterns, 
and an optional end anchor pattern (see [Anchors](anchors.md)).

<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" class="railroad-diagram" width="753.5" height="117" viewBox="0 0 753.5 117">
  <g transform="translate(.5 .5)">
    <g>
      <path d="M20 63v20m0 -10h20"></path>
    </g>
    <g>
      <path d="M40 73h0"></path>
      <path d="M315 73h0"></path>
      <path d="M40 73a12 12 0 0 0 12 -12v-29a12 12 0 0 1 12 -12"></path>
      <g>
        <path d="M64 20h227"></path>
      </g>
      <path d="M291 20a12 12 0 0 1 12 12v29a12 12 0 0 0 12 12"></path>
      <path d="M40 73h24"></path>
      <g>
        <path d="M64 73h0"></path>
        <path d="M291 73h0"></path>
        <path d="M64 73a12 12 0 0 0 12 -12v-8a12 12 0 0 1 12 -12"></path>
        <g>
          <path d="M88 41h8.5"></path>
          <path d="M258.5 41h8.5"></path>
          <g class="terminal ">
            <path d="M96.5 41h0"></path>
            <path d="M201.5 41h0"></path>
            <rect x="96.5" y="30" width="105" height="22" rx="10" ry="10"></rect>
            <text x="149" y="45">line&#95;start</text>
          </g>
          <path d="M201.5 41h10"></path>
          <path d="M211.5 41h10"></path>
          <g class="terminal ">
            <path d="M221.5 41h0"></path>
            <path d="M258.5 41h0"></path>
            <rect x="221.5" y="30" width="37" height="22" rx="10" ry="10"></rect>
            <text x="240" y="45">()</text>
          </g>
        </g>
        <path d="M267 41a12 12 0 0 1 12 12v8a12 12 0 0 0 12 12"></path>
        <path d="M64 73h24"></path>
        <g>
          <path d="M88 73h0"></path>
          <path d="M267 73h0"></path>
          <g class="terminal ">
            <path d="M88 73h0"></path>
            <path d="M210 73h0"></path>
            <rect x="88" y="62" width="122" height="22" rx="10" ry="10"></rect>
            <text x="149" y="77">string&#95;start</text>
          </g>
          <path d="M210 73h10"></path>
          <path d="M220 73h10"></path>
          <g class="terminal ">
            <path d="M230 73h0"></path>
            <path d="M267 73h0"></path>
            <rect x="230" y="62" width="37" height="22" rx="10" ry="10"></rect>
            <text x="248.5" y="77">()</text>
          </g>
        </g>
        <path d="M267 73h24"></path>
      </g>
      <path d="M291 73h24"></path>
    </g>
    <path d="M315 73h10"></path>
    <g>
      <path d="M325 73h0"></path>
      <path d="M445.5 73h0"></path>
      <path d="M325 73h12"></path>
      <g class="terminal ">
        <path d="M337 73h0"></path>
        <path d="M433.5 73h0"></path>
        <rect x="337" y="62" width="96.5" height="22" rx="10" ry="10"></rect>
        <text x="385.25" y="77">{pattern}</text>
      </g>
      <path d="M433.5 73h12"></path>
      <path d="M337 73a12 12 0 0 0 -12 12v0a12 12 0 0 0 12 12"></path>
      <g>
        <path d="M337 97h96.5"></path>
      </g>
      <path d="M433.5 97a12 12 0 0 0 12 -12v0a12 12 0 0 0 -12 -12"></path>
    </g>
    <path d="M445.5 73h10"></path>
    <g>
      <path d="M455.5 73h0"></path>
      <path d="M713.5 73h0"></path>
      <path d="M455.5 73a12 12 0 0 0 12 -12v-29a12 12 0 0 1 12 -12"></path>
      <g>
        <path d="M479.5 20h210"></path>
      </g>
      <path d="M689.5 20a12 12 0 0 1 12 12v29a12 12 0 0 0 12 12"></path>
      <path d="M455.5 73h24"></path>
      <g>
        <path d="M479.5 73h0"></path>
        <path d="M689.5 73h0"></path>
        <path d="M479.5 73a12 12 0 0 0 12 -12v-8a12 12 0 0 1 12 -12"></path>
        <g>
          <path d="M503.5 41h8.5"></path>
          <path d="M657 41h8.5"></path>
          <g class="terminal ">
            <path d="M512 41h0"></path>
            <path d="M600 41h0"></path>
            <rect x="512" y="30" width="88" height="22" rx="10" ry="10"></rect>
            <text x="556" y="45">line&#95;end</text>
          </g>
          <path d="M600 41h10"></path>
          <path d="M610 41h10"></path>
          <g class="terminal ">
            <path d="M620 41h0"></path>
            <path d="M657 41h0"></path>
            <rect x="620" y="30" width="37" height="22" rx="10" ry="10"></rect>
            <text x="638.5" y="45">()</text>
          </g>
        </g>
        <path d="M665.5 41a12 12 0 0 1 12 12v8a12 12 0 0 0 12 12"></path>
        <path d="M479.5 73h24"></path>
        <g>
          <path d="M503.5 73h0"></path>
          <path d="M665.5 73h0"></path>
          <g class="terminal ">
            <path d="M503.5 73h0"></path>
            <path d="M608.5 73h0"></path>
            <rect x="503.5" y="62" width="105" height="22" rx="10" ry="10"></rect>
            <text x="556" y="77">string&#95;end</text>
          </g>
          <path d="M608.5 73h10"></path>
          <path d="M618.5 73h10"></path>
          <g class="terminal ">
            <path d="M628.5 73h0"></path>
            <path d="M665.5 73h0"></path>
            <rect x="628.5" y="62" width="37" height="22" rx="10" ry="10"></rect>
            <text x="647" y="77">()</text>
          </g>
        </g>
        <path d="M665.5 73h24"></path>
      </g>
      <path d="M689.5 73h24"></path>
    </g>
    <path d="M 713.5 73 h 20 m 0 -10 v 20"></path>
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

Non-anchor patterns can be [Characters](characters.md), [Alternatives](alternatives.md), [Groups](groups.md), 
[Lookarounds](lookarounds.md), and [Modes](modes.md). 
All character patterns can be quantified -- see [Quantifiers](quantifiers.md) -- except word boundaries, which are not character consuming.
Groups and alternatives can also be quantified, but not lookarounds or modes.

Whitespace and Python-style # [comments](comments.md) are ignored. So, this:

```
# Floating-point number

digit() * 0, ...
period()
digit() * 1, ...
all (
  "e"
  digit() * 1, ...
) * 0, 1
```

is equivalent to this:

```
digit() * 0, ... period() digit() * 1, ... all ("e" digit() * 1, ... ) * 0, 1
```
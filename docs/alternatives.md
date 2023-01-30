# Alternatives

TODO

<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" class="railroad-diagram" width="601.5" height="107" viewBox="0 0 601.5 107">
  <g transform="translate(.5 .5)">
    <g>
      <path d="M20 34v20m0 -10h20"></path>
    </g>
    <path d="M40 44h10"></path>
    <g class="terminal ">
      <path d="M50 44h0"></path>
      <path d="M95.5 44h0"></path>
      <rect x="50" y="33" width="45.5" height="22" rx="10" ry="10"></rect>
      <text x="72.75" y="48">any</text>
    </g>
    <path d="M95.5 44h10"></path>
    <g>
      <path d="M105.5 44h0"></path>
      <path d="M324 44h0"></path>
      <path d="M105.5 44a12 12 0 0 0 12 -12v0a12 12 0 0 1 12 -12"></path>
      <g>
        <path d="M129.5 20h170.5"></path>
      </g>
      <path d="M300 20a12 12 0 0 1 12 12v0a12 12 0 0 0 12 12"></path>
      <path d="M105.5 44h24"></path>
      <g>
        <path d="M129.5 44h0"></path>
        <path d="M300 44h0"></path>
        <g class="terminal ">
          <path d="M129.5 44h0"></path>
          <path d="M166.5 44h0"></path>
          <rect x="129.5" y="33" width="37" height="22" rx="10" ry="10"></rect>
          <text x="148" y="48">as</text>
        </g>
        <path d="M166.5 44h10"></path>
        <path d="M176.5 44h10"></path>
        <g class="terminal ">
          <path d="M186.5 44h0"></path>
          <path d="M300 44h0"></path>
          <rect x="186.5" y="33" width="113.5" height="22" rx="10" ry="10"></rect>
          <text x="243.25" y="48">{identfier}</text>
        </g>
      </g>
      <path d="M300 44h24"></path>
    </g>
    <path d="M324 44h10"></path>
    <g class="terminal ">
      <path d="M334 44h0"></path>
      <path d="M362.5 44h0"></path>
      <rect x="334" y="33" width="28.5" height="22" rx="10" ry="10"></rect>
      <text x="348.25" y="48">(</text>
    </g>
    <path d="M362.5 44h10"></path>
    <path d="M372.5 44h10"></path>
    <g>
      <path d="M382.5 44h0"></path>
      <path d="M503 44h0"></path>
      <path d="M382.5 44h12"></path>
      <g class="terminal ">
        <path d="M394.5 44h0"></path>
        <path d="M491 44h0"></path>
        <rect x="394.5" y="33" width="96.5" height="22" rx="10" ry="10"></rect>
        <text x="442.75" y="48">{pattern}</text>
      </g>
      <path d="M491 44h12"></path>
      <path d="M394.5 44a12 12 0 0 0 -12 12v8a12 12 0 0 0 12 12"></path>
      <g class="terminal ">
        <path d="M394.5 76h34"></path>
        <path d="M457 76h34"></path>
        <rect x="428.5" y="65" width="28.5" height="22" rx="10" ry="10"></rect>
        <text x="442.75" y="80">|</text>
      </g>
      <path d="M491 76a12 12 0 0 0 12 -12v-8a12 12 0 0 0 -12 -12"></path>
    </g>
    <path d="M503 44h10"></path>
    <path d="M513 44h10"></path>
    <g class="terminal ">
      <path d="M523 44h0"></path>
      <path d="M551.5 44h0"></path>
      <rect x="523" y="33" width="28.5" height="22" rx="10" ry="10"></rect>
      <text x="537.25" y="48">)</text>
    </g>
    <path d="M551.5 44h10"></path>
    <path d="M 561.5 44 h 20 m 0 -10 v 20"></path>
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

> NOTE - I don't think 'any' is the right keyword here. Consider it a placeholder.
> Given the "match (a) <predicate/pattern>" template, I think a better keyword or
> phrase here might be "one" or "one_of". 
> For example:

```
one ("Alice" | "Bob" | "Carol")
one_of ("Alice" | "Bob" | "Carol")
```

# Groups

To create an &uuml;ber pattern that consists of several patterns in sequence, use the `group` predicate:

<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" class="railroad-diagram" width="618.5" height="120" viewBox="0 0 618.5 120">
  <g transform="translate(.5 .5)">
    <g>
      <path d="M20 34v20m0 -10h20"></path>
    </g>
    <path d="M40 44h10"></path>
    <g class="terminal ">
      <path d="M50 44h0"></path>
      <path d="M112.5 44h0"></path>
      <rect x="50" y="33" width="62.5" height="22" rx="10" ry="10"></rect>
      <text x="81.25" y="48">group</text>
    </g>
    <path d="M112.5 44h10"></path>
    <g>
      <path d="M122.5 44h0"></path>
      <path d="M341 44h0"></path>
      <path d="M122.5 44a12 12 0 0 0 12 -12v0a12 12 0 0 1 12 -12"></path>
      <g>
        <path d="M146.5 20h170.5"></path>
      </g>
      <path d="M317 20a12 12 0 0 1 12 12v0a12 12 0 0 0 12 12"></path>
      <path d="M122.5 44h24"></path>
      <g>
        <path d="M146.5 44h0"></path>
        <path d="M317 44h0"></path>
        <g class="terminal ">
          <path d="M146.5 44h0"></path>
          <path d="M183.5 44h0"></path>
          <rect x="146.5" y="33" width="37" height="22" rx="10" ry="10"></rect>
          <text x="165" y="48">as</text>
        </g>
        <path d="M183.5 44h10"></path>
        <path d="M193.5 44h10"></path>
        <g class="terminal ">
          <path d="M203.5 44h0"></path>
          <path d="M317 44h0"></path>
          <rect x="203.5" y="33" width="113.5" height="22" rx="10" ry="10"></rect>
          <text x="260.25" y="48">{identfier}</text>
        </g>
      </g>
      <path d="M317 44h24"></path>
    </g>
    <path d="M341 44h10"></path>
    <g class="terminal ">
      <path d="M351 44h0"></path>
      <path d="M379.5 44h0"></path>
      <rect x="351" y="33" width="28.5" height="22" rx="10" ry="10"></rect>
      <text x="365.25" y="48">(</text>
    </g>
    <path d="M379.5 44h10"></path>
    <path d="M389.5 44h10"></path>
    <g>
      <path d="M399.5 44h0"></path>
      <path d="M520 44h0"></path>
      <path d="M399.5 44h12"></path>
      <g class="terminal ">
        <path d="M411.5 44h0"></path>
        <path d="M508 44h0"></path>
        <rect x="411.5" y="33" width="96.5" height="22" rx="10" ry="10"></rect>
        <text x="459.75" y="48">{pattern}</text>
      </g>
      <path d="M508 44h12"></path>
      <path d="M411.5 44a12 12 0 0 0 -12 12v21a12 12 0 0 0 12 12"></path>
      <g>
        <path d="M411.5 89h10"></path>
        <path d="M498 89h10"></path>
        <path d="M421.5 89a12 12 0 0 0 12 -12v0a12 12 0 0 1 12 -12"></path>
        <g>
          <path d="M445.5 65h28.5"></path>
        </g>
        <path d="M474 65a12 12 0 0 1 12 12v0a12 12 0 0 0 12 12"></path>
        <path d="M421.5 89h24"></path>
        <g class="terminal ">
          <path d="M445.5 89h0"></path>
          <path d="M474 89h0"></path>
          <rect x="445.5" y="78" width="28.5" height="22" rx="10" ry="10"></rect>
          <text x="459.75" y="93">,</text>
        </g>
        <path d="M474 89h24"></path>
      </g>
      <path d="M508 89a12 12 0 0 0 12 -12v-21a12 12 0 0 0 -12 -12"></path>
    </g>
    <path d="M520 44h10"></path>
    <path d="M530 44h10"></path>
    <g class="terminal ">
      <path d="M540 44h0"></path>
      <path d="M568.5 44h0"></path>
      <rect x="540" y="33" width="28.5" height="22" rx="10" ry="10"></rect>
      <text x="554.25" y="48">)</text>
    </g>
    <path d="M568.5 44h10"></path>
    <path d="M 578.5 44 h 20 m 0 -10 v 20"></path>
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

This creates a regex group.
You can name a group for later reference, using the `'as' {identifier}` clause.
For example:

```
word_boundary()
digit()
digit()
group as magic (
  digit()
  digit()
)
"-"
magic
"-"
magic
word_boundary()
```
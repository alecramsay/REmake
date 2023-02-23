# Alternatives

To match one of several alternative patterns, use the `alternative` predicate, separating the alternatives with pipes ('\|'):

<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" class="railroad-diagram" width="669.5" height="107" viewBox="0 0 669.5 107">
  <g transform="translate(.5 .5)">
    <g>
      <path d="M20 34v20m0 -10h20"></path>
    </g>
    <path d="M40 44h10"></path>
    <g class="terminal ">
      <path d="M50 44h0"></path>
      <path d="M163.5 44h0"></path>
      <rect x="50" y="33" width="113.5" height="22" rx="10" ry="10"></rect>
      <text x="106.75" y="48">alternative</text>
    </g>
    <path d="M163.5 44h10"></path>
    <g>
      <path d="M173.5 44h0"></path>
      <path d="M392 44h0"></path>
      <path d="M173.5 44a12 12 0 0 0 12 -12v0a12 12 0 0 1 12 -12"></path>
      <g>
        <path d="M197.5 20h170.5"></path>
      </g>
      <path d="M368 20a12 12 0 0 1 12 12v0a12 12 0 0 0 12 12"></path>
      <path d="M173.5 44h24"></path>
      <g>
        <path d="M197.5 44h0"></path>
        <path d="M368 44h0"></path>
        <g class="terminal ">
          <path d="M197.5 44h0"></path>
          <path d="M234.5 44h0"></path>
          <rect x="197.5" y="33" width="37" height="22" rx="10" ry="10"></rect>
          <text x="216" y="48">as</text>
        </g>
        <path d="M234.5 44h10"></path>
        <path d="M244.5 44h10"></path>
        <g class="terminal ">
          <path d="M254.5 44h0"></path>
          <path d="M368 44h0"></path>
          <rect x="254.5" y="33" width="113.5" height="22" rx="10" ry="10"></rect>
          <text x="311.25" y="48">{identfier}</text>
        </g>
      </g>
      <path d="M368 44h24"></path>
    </g>
    <path d="M392 44h10"></path>
    <g class="terminal ">
      <path d="M402 44h0"></path>
      <path d="M430.5 44h0"></path>
      <rect x="402" y="33" width="28.5" height="22" rx="10" ry="10"></rect>
      <text x="416.25" y="48">(</text>
    </g>
    <path d="M430.5 44h10"></path>
    <path d="M440.5 44h10"></path>
    <g>
      <path d="M450.5 44h0"></path>
      <path d="M571 44h0"></path>
      <path d="M450.5 44h12"></path>
      <g class="terminal ">
        <path d="M462.5 44h0"></path>
        <path d="M559 44h0"></path>
        <rect x="462.5" y="33" width="96.5" height="22" rx="10" ry="10"></rect>
        <text x="510.75" y="48">{pattern}</text>
      </g>
      <path d="M559 44h12"></path>
      <path d="M462.5 44a12 12 0 0 0 -12 12v8a12 12 0 0 0 12 12"></path>
      <g class="terminal ">
        <path d="M462.5 76h34"></path>
        <path d="M525 76h34"></path>
        <rect x="496.5" y="65" width="28.5" height="22" rx="10" ry="10"></rect>
        <text x="510.75" y="80">|</text>
      </g>
      <path d="M559 76a12 12 0 0 0 12 -12v-8a12 12 0 0 0 -12 -12"></path>
    </g>
    <path d="M571 44h10"></path>
    <path d="M581 44h10"></path>
    <g class="terminal ">
      <path d="M591 44h0"></path>
      <path d="M619.5 44h0"></path>
      <rect x="591" y="33" width="28.5" height="22" rx="10" ry="10"></rect>
      <text x="605.25" y="48">)</text>
    </g>
    <path d="M619.5 44h10"></path>
    <path d="M 629.5 44 h 20 m 0 -10 v 20"></path>
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

So you can precede and follow a set of alternatives with other patterns,
alternatives create a regex group.
You can name the group for later reference, using the `'alternative' {identifier}` clause.


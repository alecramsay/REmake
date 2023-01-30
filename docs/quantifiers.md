# Quantifiers

Except for non-consuming character patterns and anchor patterns, patterns can be quantified,
i.e., a number of repetitions can be specified.
The syntax is simple and regular:

<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" class="railroad-diagram" width="588.5" height="126" viewBox="0 0 588.5 126">
  <g transform="translate(.5 .5)">
    <g>
      <path d="M20 53v20m0 -10h20"></path>
    </g>
    <path d="M40 63h10"></path>
    <g class="terminal ">
      <path d="M50 63h0"></path>
      <path d="M146.5 63h0"></path>
      <rect x="50" y="52" width="96.5" height="22" rx="10" ry="10"></rect>
      <text x="98.25" y="67">{pattern}</text>
    </g>
    <path d="M146.5 63h10"></path>
    <path d="M156.5 63h10"></path>
    <g class="terminal ">
      <path d="M166.5 63h0"></path>
      <path d="M195 63h0"></path>
      <rect x="166.5" y="52" width="28.5" height="22" rx="10" ry="10"></rect>
      <text x="180.75" y="67">&#42;</text>
    </g>
    <path d="M195 63h10"></path>
    <g>
      <path d="M205 63h0"></path>
      <path d="M446.5 63h0"></path>
      <path d="M205 63a12 12 0 0 0 12 -12v-8a12 12 0 0 1 12 -12"></path>
      <g class="terminal ">
        <path d="M229 31h65.5"></path>
        <path d="M357 31h65.5"></path>
        <rect x="294.5" y="20" width="62.5" height="22" rx="10" ry="10"></rect>
        <text x="325.75" y="35">{int}</text>
      </g>
      <path d="M422.5 31a12 12 0 0 1 12 12v8a12 12 0 0 0 12 12"></path>
      <path d="M205 63h24"></path>
      <g>
        <path d="M229 63h8.5"></path>
        <path d="M414 63h8.5"></path>
        <g class="terminal ">
          <path d="M237.5 63h0"></path>
          <path d="M300 63h0"></path>
          <rect x="237.5" y="52" width="62.5" height="22" rx="10" ry="10"></rect>
          <text x="268.75" y="67">{int}</text>
        </g>
        <path d="M300 63h10"></path>
        <path d="M310 63h10"></path>
        <g class="terminal ">
          <path d="M320 63h0"></path>
          <path d="M348.5 63h0"></path>
          <rect x="320" y="52" width="28.5" height="22" rx="10" ry="10"></rect>
          <text x="334.25" y="67">,</text>
        </g>
        <path d="M348.5 63h10"></path>
        <path d="M358.5 63h10"></path>
        <g class="terminal ">
          <path d="M368.5 63h0"></path>
          <path d="M414 63h0"></path>
          <rect x="368.5" y="52" width="45.5" height="22" rx="10" ry="10"></rect>
          <text x="391.25" y="67">...</text>
        </g>
      </g>
      <path d="M422.5 63h24"></path>
      <path d="M205 63a12 12 0 0 1 12 12v8a12 12 0 0 0 12 12"></path>
      <g>
        <path d="M229 95h0"></path>
        <path d="M422.5 95h0"></path>
        <g class="terminal ">
          <path d="M229 95h0"></path>
          <path d="M291.5 95h0"></path>
          <rect x="229" y="84" width="62.5" height="22" rx="10" ry="10"></rect>
          <text x="260.25" y="99">{int}</text>
        </g>
        <path d="M291.5 95h10"></path>
        <path d="M301.5 95h10"></path>
        <g class="terminal ">
          <path d="M311.5 95h0"></path>
          <path d="M340 95h0"></path>
          <rect x="311.5" y="84" width="28.5" height="22" rx="10" ry="10"></rect>
          <text x="325.75" y="99">,</text>
        </g>
        <path d="M340 95h10"></path>
        <path d="M350 95h10"></path>
        <g class="terminal ">
          <path d="M360 95h0"></path>
          <path d="M422.5 95h0"></path>
          <rect x="360" y="84" width="62.5" height="22" rx="10" ry="10"></rect>
          <text x="391.25" y="99">{int}</text>
        </g>
      </g>
      <path d="M422.5 95a12 12 0 0 0 12 -12v-8a12 12 0 0 1 12 -12"></path>
    </g>
    <g>
      <path d="M446.5 63h0"></path>
      <path d="M548.5 63h0"></path>
      <path d="M446.5 63a12 12 0 0 0 12 -12v0a12 12 0 0 1 12 -12"></path>
      <g>
        <path d="M470.5 39h54"></path>
      </g>
      <path d="M524.5 39a12 12 0 0 1 12 12v0a12 12 0 0 0 12 12"></path>
      <path d="M446.5 63h24"></path>
      <g class="terminal ">
        <path d="M470.5 63h0"></path>
        <path d="M524.5 63h0"></path>
        <rect x="470.5" y="52" width="54" height="22" rx="10" ry="10"></rect>
        <text x="497.5" y="67">lazy</text>
      </g>
      <path d="M524.5 63h24"></path>
    </g>
    <path d="M 548.5 63 h 20 m 0 -10 v 20"></path>
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

Use an ellipsis ('...') to indicate no maximum number of repetitions.
All of these are valid quantifiers:

```
{pattern} * 10      # Exactly 10 times
{pattern} * 0, 1    # Zero or one time (optional)
{pattern} * 1, ...  # One or more times
```

By default, quantifiers are "greedy." To do "lazy" matching instead, use the 'lazy' option.
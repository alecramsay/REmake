# Lookarounds

To match a pattern before or after another pattern without consuming any input, use the 'predeced_by' and 'followed_by' predicates:

<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" class="railroad-diagram" width="572.5" height="139" viewBox="0 0 572.5 139">
  <g transform="translate(.5 .5)">
    <g>
      <path d="M20 53v20m0 -10h20"></path>
    </g>
    <g>
      <path d="M40 63h0"></path>
      <path d="M133.5 63h0"></path>
      <path d="M40 63a12 12 0 0 0 12 -12v0a12 12 0 0 1 12 -12"></path>
      <g>
        <path d="M64 39h45.5"></path>
      </g>
      <path d="M109.5 39a12 12 0 0 1 12 12v0a12 12 0 0 0 12 12"></path>
      <path d="M40 63h24"></path>
      <g class="terminal ">
        <path d="M64 63h0"></path>
        <path d="M109.5 63h0"></path>
        <rect x="64" y="52" width="45.5" height="22" rx="10" ry="10"></rect>
        <text x="86.75" y="67">not</text>
      </g>
      <path d="M109.5 63h24"></path>
    </g>
    <g>
      <path d="M133.5 63h0"></path>
      <path d="M343.5 63h0"></path>
      <path d="M133.5 63a12 12 0 0 0 12 -12v-8a12 12 0 0 1 12 -12"></path>
      <g>
        <path d="M157.5 31h0"></path>
        <path d="M319.5 31h0"></path>
        <g class="terminal ">
          <path d="M157.5 31h0"></path>
          <path d="M271 31h0"></path>
          <rect x="157.5" y="20" width="113.5" height="22" rx="10" ry="10"></rect>
          <text x="214.25" y="35">followed&#95;by</text>
        </g>
        <path d="M271 31h10"></path>
        <path d="M281 31h10"></path>
        <g class="terminal ">
          <path d="M291 31h0"></path>
          <path d="M319.5 31h0"></path>
          <rect x="291" y="20" width="28.5" height="22" rx="10" ry="10"></rect>
          <text x="305.25" y="35">(</text>
        </g>
      </g>
      <path d="M319.5 31a12 12 0 0 1 12 12v8a12 12 0 0 0 12 12"></path>
      <path d="M133.5 63h24"></path>
      <g>
        <path d="M157.5 63h0"></path>
        <path d="M319.5 63h0"></path>
        <g class="terminal ">
          <path d="M157.5 63h0"></path>
          <path d="M271 63h0"></path>
          <rect x="157.5" y="52" width="113.5" height="22" rx="10" ry="10"></rect>
          <text x="214.25" y="67">preceded&#95;by</text>
        </g>
        <path d="M271 63h10"></path>
        <path d="M281 63h10"></path>
        <g class="terminal ">
          <path d="M291 63h0"></path>
          <path d="M319.5 63h0"></path>
          <rect x="291" y="52" width="28.5" height="22" rx="10" ry="10"></rect>
          <text x="305.25" y="67">(</text>
        </g>
      </g>
      <path d="M319.5 63h24"></path>
    </g>
    <path d="M343.5 63h10"></path>
    <g>
      <path d="M353.5 63h0"></path>
      <path d="M474 63h0"></path>
      <path d="M353.5 63h12"></path>
      <g class="terminal ">
        <path d="M365.5 63h0"></path>
        <path d="M462 63h0"></path>
        <rect x="365.5" y="52" width="96.5" height="22" rx="10" ry="10"></rect>
        <text x="413.75" y="67">{pattern}</text>
      </g>
      <path d="M462 63h12"></path>
      <path d="M365.5 63a12 12 0 0 0 -12 12v21a12 12 0 0 0 12 12"></path>
      <g>
        <path d="M365.5 108h10"></path>
        <path d="M452 108h10"></path>
        <path d="M375.5 108a12 12 0 0 0 12 -12v0a12 12 0 0 1 12 -12"></path>
        <g>
          <path d="M399.5 84h28.5"></path>
        </g>
        <path d="M428 84a12 12 0 0 1 12 12v0a12 12 0 0 0 12 12"></path>
        <path d="M375.5 108h24"></path>
        <g class="terminal ">
          <path d="M399.5 108h0"></path>
          <path d="M428 108h0"></path>
          <rect x="399.5" y="97" width="28.5" height="22" rx="10" ry="10"></rect>
          <text x="413.75" y="112">,</text>
        </g>
        <path d="M428 108h24"></path>
      </g>
      <path d="M462 108a12 12 0 0 0 12 -12v-21a12 12 0 0 0 -12 -12"></path>
    </g>
    <path d="M474 63h10"></path>
    <path d="M484 63h10"></path>
    <g class="terminal ">
      <path d="M494 63h0"></path>
      <path d="M522.5 63h0"></path>
      <rect x="494" y="52" width="28.5" height="22" rx="10" ry="10"></rect>
      <text x="508.25" y="67">)</text>
    </g>
    <path d="M522.5 63h10"></path>
    <path d="M 532.5 63 h 20 m 0 -10 v 20"></path>
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

These expressions create regex look behind and look ahead assertions, respectively. 
Use the `not` keyword to create negative assertions.
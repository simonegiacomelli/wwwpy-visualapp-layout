import logging

import js
import wwwpy.remote.component as wpc

logger = logging.getLogger(__name__)


class Component1(wpc.Component, tag_name='component-1'):

    def init_component(self):
        # language=html
        self.element.innerHTML = """
<div style="display: flex; gap: 1em;">
    <div style="display: flex; flex-direction: column; gap: 1em">
        <div style="display: flex; gap: 0.5em;">
            <button>Open</button>
            <button>Firmware</button>
            <button>Print</button>
            <button>Save</button>
        </div>

        <img src="https://raw.githubusercontent.com/simonegiacomelli/wwwpy-visualapp-layout/main/graph-main.png"
             height='200px'
             alt="img1">
    </div>
    <img src="https://raw.githubusercontent.com/simonegiacomelli/wwwpy-visualapp-layout/main/graph-options-h.png"
         height='240px'
         alt="some">
</div>

"""

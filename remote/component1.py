import inspect
import wwwpy.remote.component as wpc
import js

import logging

logger = logging.getLogger(__name__)


class Component1(wpc.Component, tag_name='component-1'):
    slButton1: js.HTMLElement = wpc.element()
    img1: js.HTMLImageElement = wpc.element()
    button1: js.HTMLButtonElement = wpc.element()
    button2: js.HTMLButtonElement = wpc.element()
    button3: js.HTMLButtonElement = wpc.element()
    button4: js.HTMLButtonElement = wpc.element()

    def init_component(self):
        # language=html
        self.element.innerHTML = """<div>component-1</div>
<sl-button data-name="slButton1">slButton1</sl-button>

<hr>
<div style="display: flex; gap: 1em;">
<div style="display: flex; flex-direction: column; gap: 1em">
    <div style="display: flex; gap: 0.5em;">
        <button data-name="button1">Open</button>
        <button data-name="button2">Firmware</button>
        <button data-name="button3">Print</button>
        <button data-name="button4">Save</button>
    </div>

    <img data-name="img1"
         src="https://images.unsplash.com/photo-1517331156700-3c241d2b4d83?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=90"
         alt="img1">
</div>
<img
         src="https://images.unsplash.com/photo-1517331156700-3c241d2b4d83?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=90"
         alt="some">
</div>

<hr>
<div style="display: flex">
    <div style="width: 30%;">Host:</div>
    <div style="flex: 1;"><input data-name="input1" placeholder="input1" style="width: 90%;"></div>
    <div style="display: flex; width: 30%;">
        <div style="width: 4em;"> Port:</div>
        <div style="flex: 1;"><input data-name="input1" placeholder="input1" style="width: 100%;"></div>
    </div>
</div>
<hr>
"""
    
    async def slButton1__click(self, event):
        logger.debug(f'{inspect.currentframe().f_code.co_name} event fired %s', event)
    

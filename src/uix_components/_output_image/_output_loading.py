from uix import Element
from uix.elements import image, div

style = """
@keyframes loading-bar {
    0% {
        width: 0%;
        background-color: #00573d;
    }

    100% {
        background-color: #333333;
        width: 100%;
    }
}

@keyframes ping-black {
    0% {
        opacity: 0.7;
    }
    75% {
        opacity: 1;
    }
    100% {
        opacity: 0.7;
    }
}

.loading-bar {
    border-radius: 3px;
    animation: loading-bar 10000ms ease-in-out forwards, ping-black 1.5s infinite;
}

.ait-search-logo {
    position: absolute;
    top: 45%;
    left: 45%;
    }

    hidden {
    display: none;
}"""

def register_resources(cls):
    cls.register_style("output_loading_css", style)
    return cls

@register_resources
class output_loading(Element):
    def __init__(self, id=None):
        super().__init__(id=id)
        (
            self
                .cls("wall hall")
                .style("justify-content","flex-start")
                .style("gap","0")
                .style("position","relative")
        )

        with self:
            with div().cls("hall loading-bar").style("width","0%"):
                pass
            with div().cls("ait-search-logo"):
                image(value="my_images/AIT_AI_LOGO.png").cls("logo").style("height","100px")

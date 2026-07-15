import document
elem = document.createElement("script")
elem.innerHTML = "alert('abc')"
head = document.getElementsByTagName("head")[0]
head.appendChild(elem)
head.removeChild(elem)
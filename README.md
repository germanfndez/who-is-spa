# Who is **Single Page Application** (SPA)

_A single-page application (SPA) is a web application or website that interacts with the user by dynamically rewriting the current web page with new data from the web server, instead of the default method of a web browser loading entire new pages. The goal is faster transitions that make the website feel more like a native app. [Read more](https://en.wikipedia.org/wiki/Single-page_application)_

## Goal

The goal of this project is to create a **single page application** without using any library or framework, just standard JavaScript while explaining what SPAs are.
This project is **not intended to be used in production, it is just an experiment.**

## How it works

Everything starts in the `index.html`, there we find a simple `<main>` which is going to be our container where all our content will go. Finally we have our `main.js`

`main.js` => here we have two events which will be pending the `load` and `hashchange` (the address or route has changed), when the event is invoked, our `router` - `onRouteChanged` function is in charge of the functionality.

And **finally**, our router it handles **according to the url path render the appropriate (`component` or `pages`)**.

## Check now

The project is deployed on the [**Vercel**](https://vercel.com/) platform.

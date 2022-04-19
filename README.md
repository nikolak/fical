# fiCal

Simple filtering service for remote iCal calendars (fiCal = filter iCal, very creative I know)

_Very_ simple application that provides a simple one page web interface for convenience.

It allows inputting remote ical URL, and then a list of keywords. Then it fetches the remote ical and filters out
all events that do not have any of the keywords in the event name. Basically it acts as a proxy between the client and the server
and it filters out events before handing over data to the client.

I wrote this because our company uses personio.com, which is absolute trash when it comes to calendar. Exporting "My Calendar"
in that Godforsaken app means I export the leaves of every employee, holidays, etc in the iCal. Which is kinda shitty, and something I absolutely do not want. 
Since they refuse to do even the absolute minimum to implement this functionality, and I have multiple use cases for having my 
own vacations in my calendar app (which doesn't support client side filtering) I wrote this within 30 min over a weekend.

To say that this is not intended for any kind of production/scalable environment would be an understatement, but that being said
it does work for me without any issues - so I decided to add a small web UI for it and publish it on GitHub as perhaps others might
find it useful as well.

You can look at the included `docker-compose.yml` for an example how to run it yourself. A functional version is available on https://fical.nikolak.com/
but it comes without any guarantees of uptime or similar.

Note: During my testing I've noticed that google calendar is being weird, and seems to reject long urls - which are completely within the spec. Google
seems to impose limit of 256chars for the URL length, which are very easy to reach with the base64 encoding this uses.

I may add a persistent storage for allowing shorter URLs, but for now I do not have a use case for this - if someone wants to contribute it, feel free to do so.

As a workaround URL shortener like bitly or similar will work just fine.

# License

MIT License

Copyright (c) 2022 Nikola Kovacevic

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

# R03 development note

The first local certificate run stopped before any assertions because the call site passed four arguments to a three-argument `delays(a, b, gaps)` helper (`TypeError: delays() takes 3 positional arguments but 4 were given`). Corrected the call to pass the candidate gap vector only, then reran from a clean process. This was a certificate wiring error, not evidence about the optimization claim; the successful stdout is kept separately in `probe.log`.

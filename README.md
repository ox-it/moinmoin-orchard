moinmoin-orchard
=================

A simple [MoinMoin][] theme based on [Twitter Bootstrap][],[moinmoin-memodump][], and the excellent HTML5 CSS3 template [extent][]. **You need to purchase a license for extent if you would like to use this theme.**

Tested with MoinMoin 1.9.7 on Python 2.7.5.


Install
-------

1. Get files by cloning the repository or download a zip and unpack it.  
   To clone:

    ```console
    $ git clone https://github.com/ox-it/moinmoin-orchard.git
    ```

2. Copy `orchard.py` into plugin directory `data/plugin/theme/`.
   Location of the directory varies according to how you installed MoinMoin.

3. Copy directory `orchard` into static files directory `MoinMoin/web/static/htdocs/`.
   Again location of that directory will vary. It could be:
    * `/usr/share/moin/htdocs` if you installed MoinMoin from Ubuntu package
    * `/usr/local/lib/python2.7/dist-packages/MoinMoin/web/static/htdocs` if you installed MoinMoin from zip
    * and so on

4. Done!
   If you run MoinMoin on a server, you might have to terminate running MoinMoin processes to reflect changes.  
   e.g. on Ubuntu:

    ```console
    $ pkill moin
    ```


How to use
----------

There are two ways to apply the theme.

### As your personal theme, keeping default theme unchanged ###

* Log into your wiki and go to user preferences page.
  (**Settings** near the upper left corner, then **Preferences**)
* Choose **orchard** from Preferred theme dropdown box.
* Hit *save* button at the bottom of the page.

### As the default theme ###

Edit `wikiconfig.py` to change `theme_default` and possibly `theme_force`.

```python
    theme_default = 'orchard'
    theme_force = True
```

Please note that indentations are important in python codes, and here you must
indent the line by exactly 4 spaces.


Customization
-------------

* TODO

License and copyrights
----------------------

* Copyright 2014 dossist, mjung, and University of Oxford IT Services.  
* This theme is licensed under [GNU GPL][] except for the extent theme CSS and Javascript.
* [Twitter Bootstrap][] is copyrighted by Twitter, Inc and licensed under [the MIT license][MIT].  
* [MoinMoin][] is copyrighted by [The MoinMoin development team](https://moinmo.in/MoinCoreTeamGroup) and licensed under [GNU GPL][].  
* Icons and some part of CSS were taken from the default modernized theme.  



[MoinMoin]: https://moinmo.in/
[Twitter Bootstrap]: http://getbootstrap.com/
[Wiki Home]: https://github.com/dossist/moinmoin-memodump/wiki
[Wiki EditMenu]: https://github.com/dossist/moinmoin-memodump/wiki/EditMenu
[Wiki Translation]: https://github.com/dossist/moinmoin-memodump/wiki/Translation
[Wiki Screenshots]: https://github.com/dossist/moinmoin-memodump/wiki/Screenshots
[GNU GPL]: http://www.gnu.org/licenses/gpl
[MIT]: https://github.com/twbs/bootstrap/blob/master/LICENSE
[extent]: themeforest.net/item/extent-premium-multipurpose-responsive-template/10113977
[moinmoin-memodump]: https://github.com/dossist/moinmoin-memodump
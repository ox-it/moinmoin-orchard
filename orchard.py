# coding=utf8
# -*- coding: utf8 -*-
# vim: set fileencoding=utf8 :
"""
    MoinMoin - Orchard theme

    Based on memodump theme in MoinMoin

    Config variables:
        Following variables and methods in wikiconfig.py will change something in the theme.

        memodump_menuoverride
            Overrides menu elements.

        memodump_menu_def(request)
            Additional data dictionary of menu items.

        memodump_hidelocation
            Overrides list of page names that should have no location area.
            e.g. [page_front_page, u'SideBar', ]

    References:
        How to edit menu items:
            https://github.com/dossist/moinmoin-memodump/wiki/EditMenu
        Tips:
            https://github.com/dossist/moinmoin-memodump/wiki/Tips

    @copyright: 2014 dossist.
    @license: GNU GPL, see http://www.gnu.org/licenses/gpl for details.
"""

from MoinMoin.theme import ThemeBase
import StringIO, re
from MoinMoin import wikiutil
from MoinMoin.action import get_available_actions
from MoinMoin.Page import Page

class Theme(ThemeBase):

    name = "orchard"

    _ = lambda x: x     # We don't have gettext at this moment, so we fake it
    icons = {
        # key         alt                        icon filename      w   h
        # FileAttach
        'attach':     ("%(attach_count)s",       "moin-attach.png",   16, 16),
        'info':       ("[INFO]",                 "moin-info.png",     16, 16),
        'attachimg':  (_("[ATTACH]"),            "attach.png",        32, 32),
        # RecentChanges
        'rss':        (_("[RSS]"),               "moin-rss.png",      16, 16),
        'deleted':    (_("[DELETED]"),           "moin-deleted.png",  16, 16),
        'updated':    (_("[UPDATED]"),           "moin-updated.png",  16, 16),
        'renamed':    (_("[RENAMED]"),           "moin-renamed.png",  16, 16),
        'conflict':   (_("[CONFLICT]"),          "moin-conflict.png", 16, 16),
        'new':        (_("[NEW]"),               "moin-new.png",      16, 16),
        'diffrc':     (_("[DIFF]"),              "moin-diff.png",     16, 16),
        # General
        'bottom':     (_("[BOTTOM]"),            "moin-bottom.png",   16, 16),
        'top':        (_("[TOP]"),               "moin-top.png",      16, 16),
        'www':        ("[WWW]",                  "moin-www.png",      16, 16),
        'mailto':     ("[MAILTO]",               "moin-email.png",    16, 16),
        'news':       ("[NEWS]",                 "moin-news.png",     16, 16),
        'telnet':     ("[TELNET]",               "moin-telnet.png",   16, 16),
        'ftp':        ("[FTP]",                  "moin-ftp.png",      16, 16),
        'file':       ("[FILE]",                 "moin-ftp.png",      16, 16),
        # search forms
        'searchbutton': ("[?]",                  "moin-search.png",   16, 16),
        'interwiki':  ("[%(wikitag)s]",          "moin-inter.png",    16, 16),

        # smileys (this is CONTENT, but good looking smileys depend on looking
        # adapted to the theme background color and theme style in general)
        #vvv    ==      vvv  this must be the same for GUI editor converter
        'X-(':        ("X-(",                    'angry.png',         16, 16),
        ':D':         (":D",                     'biggrin.png',       16, 16),
        '<:(':        ("<:(",                    'frown.png',         16, 16),
        ':o':         (":o",                     'redface.png',       16, 16),
        ':(':         (":(",                     'sad.png',           16, 16),
        ':)':         (":)",                     'smile.png',         16, 16),
        'B)':         ("B)",                     'smile2.png',        16, 16),
        ':))':        (":))",                    'smile3.png',        16, 16),
        ';)':         (";)",                     'smile4.png',        16, 16),
        '/!\\':       ("/!\\",                   'alert.png',         16, 16),
        '<!>':        ("<!>",                    'attention.png',     16, 16),
        '(!)':        ("(!)",                    'idea.png',          16, 16),
        ':-?':        (":-?",                    'tongue.png',        16, 16),
        ':\\':        (":\\",                    'ohwell.png',        16, 16),
        '>:>':        (">:>",                    'devil.png',         16, 16),
        '|)':         ("|)",                     'tired.png',         16, 16),
        ':-(':        (":-(",                    'sad.png',           16, 16),
        ':-)':        (":-)",                    'smile.png',         16, 16),
        'B-)':        ("B-)",                    'smile2.png',        16, 16),
        ':-))':       (":-))",                   'smile3.png',        16, 16),
        ';-)':        (";-)",                    'smile4.png',        16, 16),
        '|-)':        ("|-)",                    'tired.png',         16, 16),
        '(./)':       ("(./)",                   'checkmark.png',     16, 16),
        '{OK}':       ("{OK}",                   'thumbs-up.png',     16, 16),
        '{X}':        ("{X}",                    'icon-error.png',    16, 16),
        '{i}':        ("{i}",                    'icon-info.png',     16, 16),
        '{1}':        ("{1}",                    'prio1.png',         15, 13),
        '{2}':        ("{2}",                    'prio2.png',         15, 13),
        '{3}':        ("{3}",                    'prio3.png',         15, 13),
        '{*}':        ("{*}",                    'star_on.png',       16, 16),
        '{o}':        ("{o}",                    'star_off.png',      16, 16),
    }
    del _

    stylesheets = (
        # media         basename
#        ('all',         'memodump'),
#        ('all',         'moinizer'),
        ('all',         'orchard'),
        ('all',         'style'),
    )
    stylesheets_print = (
#         ('all',         'memodump'),
#         ('all',         'moinizer'),
#         ('all',         'memoprint'),
        ('all',         'orchard'),
        ('all',         'style'),
    )
    stylesheets_projection = (
#         ('all',         'memodump'),
#         ('all',         'moinizer'),
#         ('all',         'memoslide'),
        ('all',         'orchard'),
        ('all',         'style'),
    )

    def header(self, d, **kw):
        """ Assemble wiki header
        header1: supported.
        header2: supported.

        @param d: parameter dictionary
        @rtype: unicode
        @return: page header html
        """

        html = u"""
<div id="wrap">
  <!-- HEADER -->
  <header id="header" class="horizontal-w sm-rgt-mn">
    <div class="container">
      <div class="col-md-3 col-sm-3 logo-wrap">
        <div class="logo">
          <a href="/"><img src="%(prefix)s/%(theme)s/img/logo-orchard-trans-1400x382.png" width="200" id="img-logo-w1" alt="logo" class="img-logo-w1"></a>
          <a href="/"><img src="%(prefix)s/%(theme)s/img/logo-orchard-trans-1400x382.png" width="200" id="img-logo-w2" alt="logo" class="img-logo-w2"></a>
          <span class="logo-sticky"><a href="/"><img src="%(prefix)s/%(theme)s/img/logo-orchard-trans-1400x382.png" width="60" id="img-logo-w3" alt="logo" class="img-logo-w3"></a></span>
        </div> <!-- end logo -->
      </div> <!-- end col-md-3 -->
      <nav id="nav-wrap" class="nav-wrap1 col-md-9 col-sm-9">
        <div class="container">
          <!-- Search form -->
%(search)s
          <ul id="nav">
            <!-- Edit button -->
%(edit)s
            <!-- Menu -->
%(menu)s
            <!-- Login user -->
%(usermenu)s
          </ul> <!-- end #nav -->
        </div>
      </nav> <!-- end navigation -->
    </div> <!-- end container -->
  </header>

<!-- END OF MARKO -->

  <section id="wikiheader">
    <div class="container">
      <div class="col-sm-12 locationinfo">
            %(locationinfo)s
      </div>  <!-- end col-sm-12 -->
      <div class="col-sm-12 message">
        %(msg)s
      </div> <!-- end col-sm-12 -->
    </div> <!-- end container -->
  </section>

  <section id="wikicontent">
    <div class="container">
      <div class="col-sm-12"> <!-- Moinmoin wiki contents start here -->
""" % {'prefix': self.cfg.url_prefix_static,
       'theme': self.name,
       'locationinfo': self.location(d),
       'menu': self.menu(d),
       'usermenu': self.username(d),
       'search': self.searchform(d),
       'edit': self.editbutton(d),
       'msg': self.msg(d)
       # 'sidebar': self.sidebar(d),
       # 'navilinks': self.navibar(d),
       # 'commentbutton': self.commentbutton(),
       # 'trail': self.trail(d),
       #'quicklinks': self.quicklinks(d),
       }

        return html

    def editorheader(self, d, **kw):
        """
        header() for edit mode. Just set edit mode flag and call self.header().
        """
        d['edit_mode'] = 1
        return self.header(d, **kw)

    def footer(self, d, **keywords):
        """ Assemble wiki footer
        footer1: supported.
        footer2: supported.

        @param d: parameter dictionary
        @keyword ...:...
        @rtype: unicode
        @return: page footer html
        """
        page = d['page']

        html = u"""
      </div><!-- end col-sm-10 / end of page contents -->
    </div><!-- end container -->
  </section>

  <section class="blox dark cooperation">
    <div class="container">
      <hr class="vertical-space2">
      <div class="col-sm-12">
        <div class="col-sm-9 alignright partnerlogos">
          <span id="orchard-collab">Orchard is a close co-operation of </span>
          <a href="http://www.it.ox.ac.uk"><img src="%(prefix)s/%(theme)s/img/logo-itservices-568x500.png"></a>
        </div> <!-- end col-sm-9 -->
        <div class="col-sm-3 fix-btn-mrg">
          <a href="/devel/join" class="button large">JOIN US</a>
        </div>
      </div> <!-- end col-sm-12 -->
    </div> <!-- end container -->
   </section> <!-- end section -->

  <!-- Footer -->
  <footer id="footer">
    <section class="container footer-in">
      <div class="col-md-3">
        <div class="widget">
          <div class="textwidget">
            <div class="alignleft">
              <div class="vertical-space4"></div>
                <img id="logo-oxford-bottom" src="%(prefix)s/%(theme)s/img/logo-oxford-800x250.png" alt="Orchard">
              <div class="vertical-space4"></div>
            </div>
          </div>
        </div>
      </div> <!-- end col-md-3 -->
      
      <div class="col-md-3">
        <div class="widget">
          <div class="textwidget">
            <div class="vertical-space4"></div>
          </div>
        </div>
        <div class="widget">
          <div class="menu-footer-menu1-container">
            <ul id="menu-footer-menu1" class="menu">
              <li><a href="https://www.orchard.ox.ac.uk/">Home</a></li>
              <li><a href="https://docs.orchard.ox.ac.uk">Documentation</a></li>
              <li><a href="https://jss.orchard.ox.ac.uk">JAMF Software Server</a></li>
              <li><a href="https://docs.orchard.ox.ac.uk/devel">Developer's corner</a></li>
            </ul>
          </div>
        </div>
      </div> <!-- end col-md-3 -->
      
      <div class="col-md-3"></div>
        <div class="col-md-3">
          <div class="widget">
            <div class="textwidget">
              <div class="vertical-space4"></div>
              <div class="vertical-space2"></div>
            </div>
          </div>
          <div class="widget">
            <div class="socialfollow">
              <a href="#" class="twitter"><i class="fa-twitter"></i></a>
              <a href="#" class="facebook"><i class="fa-facebook"></i></a>
              <a href="#" class="dribble"><i class="fa-dribbble"></i></a>
              <a href="#" class="google"><i class="fa-google"></i></a>
              <a href="#" class="instagram"><i class="fa-instagram"></i></a>
              <div class="clear"></div>
            </div>
          </div>
          <div class="widget">
            <div class="textwidget">
              &copy; 2015 University of Oxford.<br />
              All Rights Reserved.</div>
          </div>
         </div> <!-- end col-md-3 -->
      </section> <!-- end-footer-in -->
   </footer>

  <span id="scroll-top">
    <a class="scrollup" style="display: block;"><i class="fa-chevron-up"></i></a>
  </span>
  
</div> <!-- end Wrap -->

<!-- End Document ================================================== -->

<!-- JS ================================================== -->
<script src="%(prefix)s/%(theme)s/js/jquery.plugins.js" type="text/javascript"></script>
<script src="%(prefix)s/%(theme)s/js/jquery.masonry.min.js" type="text/javascript"></script>
<script src="%(prefix)s/%(theme)s/js/mediaelement-and-player.min.js" type="text/javascript"></script>
<script src="%(prefix)s/%(theme)s/js/isotope.js" type="text/javascript"></script>
<script src="%(prefix)s/%(theme)s/layerslider/js/layerslider.transitions.js" type="text/javascript"></script>
<script src="%(prefix)s/%(theme)s/layerslider/js/layerslider.kreaturamedia.jquery.js" type="text/javascript"></script>
<script src="%(prefix)s/%(theme)s/js/sticky-custom.js" type="text/javascript"></script>
<script src="%(prefix)s/%(theme)s/js/extent-custom.js" type="text/javascript"></script>

<!-- Custom script -->
%(script)s
<!-- End JS ================================================== -->
""" % {'version': self.showversion(d, **keywords),
       'prefix': self.cfg.url_prefix_static,
       'theme': self.name,
       'script': self.script(),
      }

        return html

    # TODO do we need this?
    def script(self):
        """
        Append in-html script at the bottom of the page body.
        """
        
        return ur"""
  <script>
    +function ($) {
      // Toggle minified navbar under mobile landscape view
      $('.navbar-collapse').on('show.bs.collapse', function () {
        $('.navbar-mobile-toggle').togglejs('show');
      });
      $('.navbar-collapse').on('hidden.bs.collapse', function () {
        $('.navbar-mobile-toggle').togglejs('hide');
      });
      
      //Scroll position fix for hash anchors
      var mdAnchorFix = {
        escapeRe: /[ !"#$%&'()*+,.\/:;<=>?@\[\\\]^`{|}~]/g,
        escape: function (str) {
          return str.replace(mdAnchorFix.escapeRe, '\\$&');
        },
        rgbRe: /^rgba\(([ \t]*\d{1,3},){3}([ \t]*\d{1,3})\)$/i,
        isTransparent: function (rgbstr) {
          if (rgbstr === 'transparent') {
            return true;
          }
          rgbMatch = rgbstr.match(mdAnchorFix.rgbRe);
          if (rgbMatch) {
            return (Number(rgbMatch[2]) ? false : true);
          }
          return false;
        },
        navbarHeight: function () {
          var height = 0;
          var $navbar = $('.navbar');
          if ( !mdAnchorFix.isTransparent($navbar.css('background-color'))
               && ($navbar.css('display') !== 'none')
               && ($navbar.css('visibility') !== 'hidden') ) {
            height = $navbar.height();
          }
          return height;
        },
        jump: function () {
          origin = $('#' + mdAnchorFix.escape(location.hash.substr(1))).offset().top;
          offset = mdAnchorFix.navbarHeight() + 15;
          setTimeout(function () { window.scrollTo(0, origin - offset); }, 1);
        },
        clickWrapper: function () {
          if ( ($(this).attr('href') === location.hash)
               || !('onhashchange' in window.document.body) ) {
            setTimeout(function () { $(window).trigger("hashchange"); }, 1);
          }
        },
      };
      $('#pagebox a[href^="#"]:not([href="#"])').on("click", mdAnchorFix.clickWrapper);
      $(window).on("hashchange", mdAnchorFix.jump);
      if (location.hash) setTimeout(function () { mdAnchorFix.jump(); }, 100);
    }(jQuery);
  </script>
"""

    def location(self, d):
        """ Assemble location area on top of the page content.
        Certain pages shouldn't have location area as it feels redundant.
        Location area is excluded in FrontPage by default.
        Config variable memodump_hidelocation will override the list of 
        pages to have no location area.
        """
        html = u''
        page = d['page']
        pages_hide = [] # [self.request.cfg.page_front_page, ]
        try:
            pages_hide = self.request.cfg.memodump_hidelocation
        except AttributeError:
            pass
        if not page.page_name in pages_hide:
            html = u'''
          <div class="col-sm-6 breadcrumb"><!-- pagename -->
          %(pagename)s
          </div>
          <div class="col-sm-6 lastupdate"><!-- lastupdate -->
          %(lastupdate)s
          </div>
''' % {'pagename': self.title(d), 'lastupdate': self.lastupdate(d), }
        return html

    def lastupdate(self, d):
        """ Return html for last update in location area, if conditions are met. """
        _ = self.request.getText
        page = d['page']
        html = u''
        if self.shouldShowPageinfo(page):
            info = page.lastEditInfo()
            if info:
                html = u'<span class="lastupdate">%s %s by %s</span>' % (
                          _('Last updated at'), info['time'], info['editor'])
        return html

    def searchform(self, d):
        """
        assemble HTML code for the search form

        @param d: parameter dictionary
        @rtype: unicode
        @return: search form html
        """
        _ = self.request.getText
        form = self.request.values
        updates = {
            'search_label': _('Search:'),
            'search_hint': _('Search'),
            'search_value': wikiutil.escape(form.get('value', ''), 1),
            'search_full_label': _('Text'),
            'search_title_label': _('Titles'),
            'url': self.request.href(d['page'].page_name)
        }
        d.update(updates)

        html = u'''
          <div id="search-form">
            <a href="javascript:void(0)" class="search-form-icon"><i id="searchbox-icon" class="fa-search"></i></a>
            <div id="search-form-box" class="search-form-box">
              <form action="#" method="get">
                <input type="hidden" name="action" value="fullsearch">
                <input type="hidden" name="titlesearch" value="0">
                <input type="hidden" name="context" value="180">
                <input type="text" class="search-text-box" id="search-box" placeholder="%(search_hint)s" name="value" value="%(search_value)s">
              </form>
            </div>
          </div> <!-- end search form -->
''' % d

        return html

    def editbutton(self, d):
        """ Return an edit button html fragment.
        If the user can't edit, return a disabled edit button.
        """
        page = d['page']
        edit_mode = d.get('edit_mode', 0)

        if 'edit' in self.request.cfg.actions_excluded:
            return u""

        button = u''
        li_attr = u''

        if not (page.isWritable() and
                self.request.user.may.write(page.page_name)):
            button = self.disabledEdit()
            li_attr = u' class="edit-disabled"'
        else:
            _ = self.request.getText
            querystr = {'action': 'edit'}
            text = u'%s' % _('Edit')
            attrs = {'name': 'editlink', 'rel': 'nofollow', 'css_class': 'menu-nav-edit'}
            button = page.link_to_raw(self.request, text=text, querystr=querystr, **attrs)
            if edit_mode:
                li_attr = u' class="edit-enabled"'

        html = u'''
            <li%s>
              %s
            </li>
''' % (li_attr, button)

        return html

    def disabledEdit(self):
        """ Return a disabled edit link """
        _ = self.request.getText
        html = u'%s%s%s' % (
                   self.request.formatter.url(1, css="menu-nav-edit"),
                   _('Immutable Page'),
                   self.request.formatter.url(0)
               )
        return html

#     def commentbutton(self):
#         """
#         Return a comment toggle button html.
#         Don't check if 'Comment' is present in self.request.cfg.edit_bar
#         The button is display:none; (i.e. disappeared) by default, but will automatically appear
#         when default javascript notices there is a comment in the source.
#         """
#         _ = self.request.getText
#         html = u'''
#             <li class="toggleCommentsButton navbar-comment-toggle" style="display:none;">
#               <a href="#" class="menu-nav-comment nbcomment navbar-comment-toggle" rel="nofollow" onClick="toggleComments();return false;" data-toggle="toggle" data-target=".navbar-comment-toggle">
#                 <span class="hidden-sm">%s</span>
#               </a>
#             </li>
# ''' % _('Comments')
#         return html

    def username(self, d):
        """ Assemble the username / userprefs link as dropdown menu
        Assemble a login link instead in case of no login user.

        @param d: parameter dictionary
        @rtype: unicode
        @return: username html
        """
        request = self.request
        _ = request.getText

        userlinks = []
        userbutton = u''
        loginbutton = u''

        # Add username/homepage link for registered users. We don't care
        # if it exists, the user can create it.
        if request.user.valid and request.user.name:
            interwiki = wikiutil.getInterwikiHomePage(request)
            name = request.user.name
            aliasname = request.user.aliasname
            if not aliasname:
                aliasname = name
            title = "%s @ %s" % (aliasname, interwiki[0])
            # link to (interwiki) user homepage
            wikitag, wikiurl, wikitail, wikitag_bad = wikiutil.resolve_interwiki(self.request, *interwiki)
            wikiurl = wikiutil.mapURL(self.request, wikiurl)
            href = wikiutil.join_wiki(wikiurl, wikitail)
            homelink = (request.formatter.url(1, href, title=title, css='menu-dd-userhome', rel="nofollow") +
                       request.formatter.text(name) +
                       request.formatter.url(0))
            userbutton = homelink
            # userlinks.append(homelink)

            # link to userprefs action
            if 'userprefs' not in self.request.cfg.actions_excluded:
                userlinks.append(d['page'].link_to_raw(request, text=_('Settings'), css_class='menu-dd-userprefs',
                                                       querystr={'action': 'userprefs'}, rel='nofollow'))
            # logout link
            if request.user.auth_method in request.cfg.auth_can_logout:
                userlinks.append(d['page'].link_to_raw(request, text=_('Logout'), css_class='menu-dd-logout',
                                                       querystr={'action': 'logout', 'logout': 'logout'}, rel='nofollow'))
        else:
            query = {'action': 'login'}
            # special direct-login link if the auth methods want no input
            if request.cfg.auth_login_inputs == ['special_no_input']:
                query['login'] = '1'
            if request.cfg.auth_have_login:
                loginbutton = (d['page'].link_to_raw(request, text=_("Login"),
                                                     querystr=query, css_class='menu-nav-login', rel='nofollow'))

        if userbutton:
            userlinks_html = u'</li>\n                <li>'.join(userlinks)
            html = u'''
            <li>
              %s
              <ul class="sub-menu">
                <li>%s</li>
              </ul>
            </li> <!-- /dropdown -->
''' % (userbutton, userlinks_html)

        elif loginbutton:
            html = u'''            <li>%s</li>''' % loginbutton

        else:
            html = u''

        return html

    def menu(self, d):
        """
        Build dropdown menu html. Incompatible with original actionsMenu() method.

        Menu can be customized by adding a config variable 'memodump_menuoverride'.
        The variable will override the default menu set.
        Additional menu definitions are given via config method 'memodump_menu_def(request)'.
        See the code below or project wiki for details.

        @param d: parameter dictionary
        @rtype: string
        @return: menu html
        """
        request = self.request
        _ = request.getText
        rev = request.rev
        page = d['page']

        page_recent_changes = wikiutil.getLocalizedPage(request, u'RecentChanges')
        page_find_page = wikiutil.getLocalizedPage(request, u'FindPage')
        page_help_contents = wikiutil.getLocalizedPage(request, u'HelpContents')
        page_help_formatting = wikiutil.getLocalizedPage(request, u'HelpOnFormatting')
        page_help_wikisyntax = wikiutil.getLocalizedPage(request, u'HelpOnMoinWikiSyntax')
        page_title_index = wikiutil.getLocalizedPage(request, u'TitleIndex')
        page_word_index = wikiutil.getLocalizedPage(request, u'WordIndex')
        page_front_page = wikiutil.getFrontPage(request)
        page_sidebar = Page(request, request.getPragma('sidebar', u'SideBar'))
        quicklink = self.menuQuickLink(page)
        subscribe = self.menuSubscribe(page)

        try:
            menu = request.cfg.memodump_menuoverride
        except AttributeError:
            # default list of items in dropdown menu.
            # menu items are assembled in this order.
            # see wiki for detailed info on customization.
            menu = [
                '===== Navigation =====',
                'RecentChanges',
                'FindPage',
                'LocalSiteMap',
#                '===== User =====',
                'quicklink',
                'subscribe',
                '__separator__',
                '===== Help =====',
                'HelpContents',
                'HelpOnMoinWikiSyntax',
                '__separator__',
                '===== Display =====',
                'AttachFile',
                'info',
                'raw',
                'print',
                '__separator__',
                '===== Edit =====',
                'RenamePage',
                'DeletePage',
                'revert',
                'CopyPage',
                'Load',
                'Save',
                'Despam',
                'editSideBar',
            ]

        # menu element definitions
        menu_def = {
            'raw': {
                # Title for this menu entry
                'title': _('Raw Text'),
                # href and args are for normal entries ('special': False), otherwise ignored.
                # 'href': Nonexistent or empty for current page
                'href': '',
                # 'args': {'query1': 'value1', 'query2': 'value2', }
                # Optionally specify this for <a href="href?query1=value1&query2=value2">
                # If href and args are both nonexistent or empty, key is automatically interpreted to be an action name
                # and href and args are automatically set.
                'args': '',
                # 'special' can be:
                #   'disabled', 'removed', 'separator' or 'header' for whatever they say,
                #    False, None or nonexistent for normal menu display.
                # 'separator' and 'header' are automatically removed when there are no entries to show among them.
                'special': False,
            },
            'print': {'title': _('Print View'), },
            'refresh': {
                'title': _('Delete Cache'),
                'special': not (self.memodumpIsAvailableAction(page, 'refresh') and page.canUseCache()) and 'removed',
            },
            'SpellCheck': {'title': _('Check Spelling'), },
            'RenamePage': {'title': _('Rename Page'), },
            'CopyPage':   {'title': _('Copy Page'), },
            'DeletePage': {'title': _('Delete Page'), },
            'LikePages':  {'title': _('Like Pages'), },
            'LocalSiteMap': {'title': _('Local Site Map'), },
            'MyPages':    {'title': _('My Pages'), },
            'SubscribeUser': {
                'title': _('Subscribe User'),
                'special': not (self.memodumpIsAvailableAction(page, 'SubscribeUser')
                                and request.user.may.admin(page.page_name)) and 'removed',
            },
            'Despam': {
                'title': _('Remove Spam'),
                'special': not (self.memodumpIsAvailableAction(page, 'Despam') and request.user.isSuperUser()) and 'removed',
            },
            'revert': {
                'title': _('Revert to this revision'),
                'special': not (self.memodumpIsAvailableAction(page, 'revert')
                                and rev
                                and request.user.may.revert(page.page_name)) and 'removed',
            },
            'PackagePages': {'title': _('Package Pages'), },
            'RenderAsDocbook': {'title': _('Render as Docbook'), },
            'SyncPages': {'title': _('Sync Pages'), },
            'AttachFile': {'title': _('Attachments'), },
            'quicklink': {
                'title': quicklink[1], 'args': dict(action=quicklink[0], rev=rev),
                'special': not quicklink[0] and 'removed',
            },
            'subscribe': {
                'title': subscribe[1], 'args': dict(action=subscribe[0], rev=rev),
                'special': not subscribe[0] and 'removed',
            },
            'info': {'title': _('Info'), },
# menu items not in menu_def will be assumed to be action names,
# and receive appropriate title, href, and args automatically.
#           'Load': {'title': _('Load'), },
#           'Save': {'title': _('Save'), },
            # menu decorations
            '__separator__':   {'title': _('------------------------'), 'special': 'separator', },
            '----':            {'title': _('------------------------'), 'special': 'separator', },
            '-----':           {'title': _('------------------------'), 'special': 'separator', },
            '------':          {'title': _('------------------------'), 'special': 'separator', },
            '-------':         {'title': _('------------------------'), 'special': 'separator', },
            '--------':        {'title': _('------------------------'), 'special': 'separator', },
            '---------':       {'title': _('------------------------'), 'special': 'separator', },
            '----------':      {'title': _('------------------------'), 'special': 'separator', },
            # header example
            '__title_navigation__': {'title': _('Navigation'), 'special': 'header', },
            # useful pages
            'RecentChanges':   {'title': page_recent_changes.page_name, 'href': page_recent_changes.url(request)},
            'FindPage':        {'title': page_find_page.page_name, 'href': page_find_page.url(request)},
            'HelpContents':    {'title': page_help_contents.page_name, 'href': page_help_contents.url(request)},
            'HelpOnFormatting': {'title': page_help_formatting.page_name, 'href': page_help_formatting.url(request)},
            'HelpOnMoinWikiSyntax': {'title': page_help_wikisyntax.page_name, 'href': page_help_wikisyntax.url(request)},
            'TitleIndex':      {'title': page_title_index.page_name, 'href': page_title_index.url(request)},
            'WordIndex':       {'title': page_word_index.page_name, 'href': page_word_index.url(request)},
            'FrontPage':       {'title': page_front_page.page_name, 'href': page_front_page.url(request)},
            'SideBar':         {'title': page_sidebar.page_name, 'href': page_sidebar.url(request)},
            'editSideBar': {
                'title': _('Edit SideBar'), 'href': page_sidebar.url(request),
                'args': dict(action='edit'),
                'special': not self.memodumpIsEditablePage(page_sidebar) and 'removed'
            },
        }

        # register state determining functions on request for use in config
        request.memodumpIsAvailableAction = self.memodumpIsAvailableAction
        request.memodumpIsEditablePage = self.memodumpIsEditablePage

        try:
            menu_def.update(request.cfg.memodump_menu_def(request))
        except AttributeError:
            pass

        compiled = self.menuCompile(d, menu, menu_def)
        menubody = self.menuRender(compiled)

        if menubody:
            html = u'''
            <li>
              <a href="#" data-description="start here">%s</a>
              <ul class="sub-menu mega wikimenu">
                <li>
                  <div class="col-sm-12">
                    <div class="col-sm-3">
%s
                  </div>
                </li>
              </ul> <!-- end sub-menu -->
            </li> <!-- end homes -->
''' % ('Wiki', menubody) # (_('Menu'), menubody)
        else:
            html = u''

        return html

    def menuGetQueryString(self, args):
        """
        Return a URL query string generated from arguments dictionary.
        {'q1': 'v1', 'q2': 'v2'} will turn into u'?q1=val&q2=val'
        """
        parts = []
        for key, value in args.iteritems():
            if value:
                parts.append(u'%s=%s' % (key, value))
        output = u'&'.join(parts)
        if output:
            output = u'?' + output
        return output

    def menuCompile(self, d, menu, menu_def):
        """
        Return a compiled list of menu data ready to input to renderer.
        """
        # subroutines to generate compiled data
        def generateAction(action, title=''):
            query = self.menuGetQueryString({'action': action, 'rev': rev})
            if not title:
                title = _(action)
            return (action, title, u'%s%s' % (page.url(request), query), False)
        def generateHeader(key, title):
            return (key, _(title), '', 'header')
        def generateSpecial(key, data):
            return (key, data.get('title', _(key)), data.get('href', u''), data.get('special', False))
        def generateNormal(key, data):
            if not data.get('href'):
                data['href'] = page.url(request)
            if data.get('args'):
                data['href'] = u'%s%s' % (data['href'], self.menuGetQueryString(data['args']))
            return (key, data.get('title', _(key)), data.get('href'), False)

        request = self.request
        _ = request.getText
        rev = request.rev
        page = d['page']
        header_re = re.compile(r'^(\=+)\s+(.+?)\s+\1$') # '= title ='

        compiled = [] # [('key', 'title', 'href', 'special'), ]
        for key in menu:
            # check if key is in the definitions list
            data = menu_def.get(key)
            if data:
                # 'removed', 'disabled', 'separator' or 'header'
                if data.get('special'):
                    compiled.append(generateSpecial(key, data))
                # normal display
                else:
                    # recognizes key as action if href and args are not provided
                    if not (data.get('href') or data.get('args')):
                        if self.memodumpIsAvailableAction(page, key):
                            compiled.append(generateAction(key, title=data.get('title', '')))
                        else:
                            continue
                    # otherwise compile as a normal menu entry
                    else:
                        compiled.append(generateNormal(key, data))
            else:
                # check if key is header string
                header_match = header_re.search(key)
                # header
                if header_match:
                    compiled.append(generateHeader(key, header_match.group(2)))
                # action not in menu_def
                elif self.memodumpIsAvailableAction(page, key):
                    compiled.append(generateAction(key))

        return self.menuThinCompiled(compiled)

    def menuThinCompiled(self, compiled):
        """
        Remove unnecessary rules and headers as well as 'removed' items from compiled menu data.
        """
        how_nice = {
            False: 0,
            'header': 2,
            'separator': 1,
            'removed': 1000,
        }
        thinned = []
        atmosphere = how_nice['separator']

        for record in reversed(compiled):
            nice = how_nice.get(record[3], 0)
            if nice < atmosphere:
                thinned.append(record)
                atmosphere = nice
            if not nice:
                atmosphere = 1000

        thinned.reverse()
        return thinned

    def menuRender(self, compiled):
        templates = {
            False:       u'                                   <li><a href="%(href)s" class="menu-dd-%(key)s">%(title)s</a></li>',
            'disabled':  u'                                   <li class="disabled"><a href="#" class="menu-dd-%(key)s" rel="nofollow">%(title)s</a></li>',
            'separator': u'                               </div>\n                               <div class="col-sm-3">\n',
            'header':    u'                                 <h4 class="subtitle">%(title)s</h4>\n                                 <ul>',
            'removed':   u'',
        }
        lines = []
        for record in compiled:
            special = record[3]
            dictionary = dict(key=record[0], title=record[1], href=record[2])
            lines.append(templates[special] % dictionary)
        return u'\n'.join(lines)

    def memodumpIsAvailableAction(self, page, action):
        """
        Return if action is available or not.
        If action starts with lowercase, return True without actually check if action exists.
        """
        request = self.request
        excluded = request.cfg.actions_excluded
        available = get_available_actions(request.cfg, page, request.user)
        return not (action in excluded or (action[0].isupper() and not action in available))

    def memodumpIsEditablePage(self, page):
        """
        Return True if page is editable for current user, False if not.

        @param page: page object
        """
        return page.isWritable() and self.request.user.may.write(page.page_name)

    def menuQuickLink(self, page):
        """
        Return quicklink action name and localized text according to status of page

        @param page: page object
        @rtype: unicode
        @return (action, text)
        """
        if not self.request.user.valid:
            return (u'', u'')

        _ = self.request.getText
        if self.request.user.isQuickLinkedTo([page.page_name]):
            action, text = u'quickunlink', _("Remove Link")
        else:
            action, text = u'quicklink', _("Add Link")
        if action in self.request.cfg.actions_excluded:
            return (u'', u'')

        return (action, text)

    def menuSubscribe(self, page):
        """
        Return subscribe action name and localized text according to status of page

        @rtype: unicode
        @return (action, text)
        """
        if not ((self.cfg.mail_enabled or self.cfg.jabber_enabled) and self.request.user.valid):
            return (u'', u'')

        _ = self.request.getText
        if self.request.user.isSubscribedTo([page.page_name]):
            action, text = 'unsubscribe', _("Unsubscribe")
        else:
            action, text = 'subscribe', _("Subscribe")
        if action in self.request.cfg.actions_excluded:
            return (u'', u'')

        return (action, text)

#     def sidebar(self, d, **keywords):
#         """ Display page called SideBar as an additional element on every page
#         content_id has been changed from the original
# 
#         @param d: parameter dictionary
#         @rtype: string
#         @return: sidebar html
#         """
# 
#         # Check which page to display, return nothing if doesn't exist.
#         sidebar = self.request.getPragma('sidebar', u'SideBar')
#         page = Page(self.request, sidebar)
#         if not page.exists():
#             return u""
#         # Capture the page's generated HTML in a buffer.
#         buffer = StringIO.StringIO()
#         self.request.redirect(buffer)
#         try:
#             page.send_page(content_only=1, content_id="sidebar-content")
#         finally:
#             self.request.redirect()
#         return u'<div class="sidebar clearfix">%s</div>' % buffer.getvalue()

#     def trail(self, d):
#         """ Assemble page trail
# 
#         @param d: parameter dictionary
#         @rtype: unicode
#         @return: trail html
#         """
#         _ = self.request.getText
#         request = self.request
#         user = request.user
#         html = u''
#         li = u'                <li>%s</li>'
# 
#         if not user.valid or user.show_page_trail:
#             trail = user.getTrail()
#             if trail:
#                 items = []
#                 for pagename in trail:
#                     try:
#                         interwiki, page = wikiutil.split_interwiki(pagename)
#                         if interwiki != request.cfg.interwikiname and interwiki != 'Self':
#                             link = (self.request.formatter.interwikilink(True, interwiki, page) +
#                                     self.shortenPagename(page) +
#                                     self.request.formatter.interwikilink(False, interwiki, page))
#                             items.append(li % link)
#                             continue
#                         else:
#                             pagename = page
# 
#                     except ValueError:
#                         pass
#                     page = Page(request, pagename)
#                     title = page.split_title()
#                     title = self.shortenPagename(title)
#                     link = page.link_to(request, title)
#                     items.append(li % link)
# 
#                 html = u'''
#             <div id="pagetrail">
#               <h4>%s</h4>
#               <ul>
# %s
#               </ul>
#             </div>
# ''' % (_('Trail'), u'\n'.join(items))
# 
#         return html

#     def quicklinks(self, d):
#         """ Assemble quicklinks
# 
#         @param d: parameter dictionary
#         @rtype: unicode
#         @return: quicklinks html
#         """
#         _ = self.request.getText
#         html = u''
#         li = u'                <li class="%s">%s</li>'
#         found = {}
#         items = []
#         current = d['page_name']
# 
#         userlinks = self.request.user.getQuickLinks()
#         for text in userlinks:
#             # non-localized anchor and texts
#             pagename, link = self.splitNavilink(text, localize=0)
#             if not pagename in found:
#                 if pagename == current:
#                     cls = 'userlink active'
#                     link = u'<a>%s</a>' % pagename
#                 else:
#                     cls = 'userlink'
#                 items.append(li % (cls, link))
#                 found[pagename] = 1
# 
#         if items:
#             html = u'''
#             <div id="quicklinks">
#               <h4>%s</h4>
#               <ul>
# %s
#               </ul>
#             </div>
# ''' % (_('Quick links'), u'\n'.join(items))
# 
#         return html

#     def navibar(self, d):
#         """ Assemble the navibar (which moved to sidebar as one of sections)
#         NavIbar, not the navbar at the page top!
# 
#         @param d: parameter dictionary
#         @rtype: unicode
#         @return: navibar html
#         """
#         request = self.request
#         _ = request.getText
#         found = {} # pages we found. prevent duplicates
#         items = [] # navibar items
#         item = u'                <li class="%s">%s</li>'
#         current = d['page_name']
# 
#         # Process config navi_bar
#         if request.cfg.navi_bar:
#             for text in request.cfg.navi_bar:
#                 pagename, link = self.splitNavilink(text)
#                 if pagename == current:
#                     cls = 'wikilink active'
#                 else:
#                     cls = 'wikilink'
#                 items.append(item % (cls, link))
#                 found[pagename] = 1
# 
#         # Add user links to wiki links, eliminating duplicates.
#         userlinks = request.user.getQuickLinks()
#         for text in userlinks:
#             # Split text without localization, user knows what he wants
#             pagename, link = self.splitNavilink(text, localize=0)
#             if not pagename in found:
#                 if pagename == current:
#                     cls = 'userlink active'
#                 else:
#                     cls = 'userlink'
#                 items.append(item % (cls, link))
#                 found[pagename] = 1
# 
#         # Add current page at end of local pages
# #       if not current in found:
# #           title = d['page'].split_title()
# #           title = self.shortenPagename(title)
# #           link = d['page'].link_to(request, title)
# #           cls = 'active'
# #           items.append(item % (cls, link))
# 
#         # Add sister pages.
#         for sistername, sisterurl in request.cfg.sistersites:
#             if sistername == request.cfg.interwikiname: # it is THIS wiki
#                 cls = 'sisterwiki active'
#                 items.append(item % (cls, sistername))
#             else:
#                 # TODO optimize performance
#                 cache = caching.CacheEntry(request, 'sisters', sistername, 'farm', use_pickle=True)
#                 if cache.exists():
#                     data = cache.content()
#                     sisterpages = data['sisterpages']
#                     if current in sisterpages:
#                         cls = 'sisterwiki'
#                         url = sisterpages[current]
#                         link = request.formatter.url(1, url) + \
#                                request.formatter.text(sistername) +\
#                                request.formatter.url(0)
#                         items.append(item % (cls, link))
# 
#         # Assemble html
#         items = u''.join(items)
#         html = u''
#         if items:
#             html = u'''
#             <div>
#               <h4>%s</h4>
#               <ul id='navibar'>
# %s
#               </ul>
#             </div>
# ''' % (_('Navigation'), items)
# 
#         return html

    def msg(self, d):
        """ Assemble the msg display

        Display a message in an alert box with an optional close button.

        @param d: parameter dictionary
        @rtype: unicode
        @return: msg display html
        """
        _ = self.request.getText
        msgs = d['msg']

        msg_conv = {
            'hint': 'alert-success',
            'info': 'alert-info',
            'warning': 'alert-warning',
            'error': 'alert-danger',
        }

        result = []
        template = u'''
        <hr class="vertical-space1">
        <div class="alert %(dismiss)s%(color)s">
          %(close)s
          %(msg)s
        </div>
'''
        param = {
            'close': u'<button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>',
            'dismiss': 'alert-dismissible ',
            'msg': '',
            'color': '',
        }

        for msg, msg_class in msgs:
            param['color'] = msg_conv['info']
            try:
                param['msg'] = msg.render()
                param['close'] = ''
                param['dismiss'] = ''
            except AttributeError:
                if msg and msg_class:
                    param['msg'] = msg
                    if msg_class in msg_conv:
                        param['color'] = msg_conv[msg_class]
                elif msg:
                    param['msg'] = msg
            finally:
                if msg:
                    result.append(template % param)
        if result:
            return u'\n'.join(result)
        else:
            return u''

    def send_title(self, text, **keywords):
        """ Capture original send_title() and rewrite DOCTYPE for html5 """

        # add some CSS class info to the body tag
        keywords['body_attr']='class="modern t-dark-w colorskin-orchard csstransforms csstransforms3d csstransitions orchard"'

        # for mobile
        additional_head = u"""
<!-- Mobile Specific Metas ================================================== -->
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">

<!-- Font ================================================== -->
<link href='http://fonts.googleapis.com/css?family=Source+Sans+Pro:300italic,400italic,400,300,600,700,900|Varela|Arapey:400,400italic' rel="stylesheet" type='text/css' >

<!-- Favicons ================================================== -->
<link rel="apple-touch-icon" sizes="57x57" href="%(prefix)s/%(theme)s/img/apple-touch-icon-57x57.png">
<link rel="apple-touch-icon" sizes="60x60" href="%(prefix)s/%(theme)s/img/apple-touch-icon-60x60.png">
<link rel="apple-touch-icon" sizes="72x72" href="%(prefix)s/%(theme)s/img/apple-touch-icon-72x72.png">
<link rel="apple-touch-icon" sizes="76x76" href="%(prefix)s/%(theme)s/img/apple-touch-icon-76x76.png">
<link rel="apple-touch-icon" sizes="114x114" href="%(prefix)s/%(theme)s/img/apple-touch-icon-114x114.png">
<link rel="apple-touch-icon" sizes="120x120" href="%(prefix)s/%(theme)s/img/apple-touch-icon-120x120.png">
<link rel="apple-touch-icon" sizes="144x144" href="%(prefix)s/%(theme)s/img/apple-touch-icon-144x144.png">
<link rel="apple-touch-icon" sizes="152x152" href="%(prefix)s/%(theme)s/img/apple-touch-icon-152x152.png">
<link rel="apple-touch-icon" sizes="180x180" href="%(prefix)s/%(theme)s/img/apple-touch-icon-180x180.png">
<link rel="icon" type="image/png" href="%(prefix)s/%(theme)s/img/favicon-32x32.png" sizes="32x32">
<link rel="icon" type="image/png" href="%(prefix)s/%(theme)s/img/favicon-194x194.png" sizes="194x194">
<link rel="icon" type="image/png" href="%(prefix)s/%(theme)s/img/favicon-96x96.png" sizes="96x96">
<link rel="icon" type="image/png" href="%(prefix)s/%(theme)s/img/android-chrome-192x192.png" sizes="192x192">
<link rel="icon" type="image/png" href="%(prefix)s/%(theme)s/img/favicon-16x16.png" sizes="16x16">
<link rel="manifest" href="%(prefix)s/%(theme)s/img/manifest.json">
<link rel="mask-icon" href="%(prefix)s/%(theme)s/img/safari-pinned-tab.svg" color="#6b902e">
<link rel="shortcut icon" href="%(prefix)s/%(theme)s/img/favicon.ico">
<meta name="msapplication-TileColor" content="#2b5797">
<meta name="msapplication-TileImage" content="%(prefix)s/%(theme)s/img/mstile-144x144.png">
<meta name="msapplication-config" content="%(prefix)s/%(theme)s/img/browserconfig.xml">
<meta name="theme-color" content="#ffffff">

<!-- JS ================================================== -->
<script src="%(prefix)s/%(theme)s/js/jquery.min.js" type="text/javascript"></script>
<script src="%(prefix)s/%(theme)s/layerslider/js/greensock.js" type="text/javascript"></script>
<!--[if lt IE 9]>
<script src="%(prefix)s/%(theme)s/js/modernizr.custom.11889.js" type="text/javascript"></script>
<script src="%(prefix)s/%(theme)s/js/respond.js" type="text/javascript"></script>
<![endif]-->
<!-- HTML5 Shiv events (end)-->
<!-- MEGA MENU -->

""" % {'prefix': self.cfg.url_prefix_static,
       'theme': self.name
      }
      
        try:
            if not self.request.cfg.memodump_additional_head:
                raise AttributeError
        except AttributeError:
            self.request.cfg.html_head = u'%s%s' % (additional_head, self.request.cfg.html_head)
            self.request.cfg.memodump_additional_head = True

        buffer = StringIO.StringIO()
        self.request.redirect(buffer)
        try:
            ThemeBase.send_title(self, text, **keywords)
        finally:
            self.request.redirect()
        html = re.sub(ur'^<!DOCTYPE HTML .*?>\n', ur'<!DOCTYPE html>\n', buffer.getvalue())
        self.request.write(html)

    def guiEditorScript(self, d):
        """ Disable default skin javascript to prevent gui edit button from automatically appearing """
        return u''

    def _stylesheet_link(self, theme, media, href, title=None):
        """ Removed charset attribute to satisfy html5 requirements """
        if theme:
            href = '%s/%s/css/%s.css' % (self.cfg.url_prefix_static, self.name, href)
        attrs = 'type="text/css" media="%s" href="%s"' % (
                media, wikiutil.escape(href, True), )
        if title:
            return '<link rel="alternate stylesheet" %s title="%s">' % (attrs, title)
        else:
            return '<link rel="stylesheet" %s>' % attrs

def execute(request):
    """
    Generate and return a theme object

    @param request: the request object
    @rtype: MoinTheme
    @return: Theme object
    """
    return Theme(request)

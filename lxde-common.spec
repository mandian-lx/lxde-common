%define git git20110808
# define Epoch only to revert from 0.5.5.1 to 0.5.5 git
Epoch: 1

Summary:	A set of default configuration for LXDE
Name:	  	lxde-common
Version:	0.5.5
Release:	%mkrel -c %git 13
License:	GPLv2+
Group:		Graphical desktop/Other
Source0: 	http://dfn.dl.sourceforge.net/sourceforge/lxde/%name-%version.tar.gz
Source1:	rosa-button-lxde.png
# Mandriva customization patch
Patch101:	lxde-common-0.5.5-pcmanfm.conf.patch
Patch102:	lxde-common-0.5.5-add-mcc-to-panel.patch
Patch103:	lxde-common-0.5.5-lxpanel-customization.patch
Patch106:	lxde-common-0.5.5-autostart.patch
Patch109:	lxde-common-0.5.5-config.patch

URL:		http://lxde.sourceforge.net/
BuildRequires:	xsltproc docbook-style-xsl
BuildArch:	noarch
#Requires:	smproxy
Suggests:	xscreensaver
Requires:	openbox
Requires:	lxpanel >= 0.5.9
Requires:	lxsession >= 0.4.1
Requires:	pcmanfm >= 0.9.10
Requires:	lxterminal
Requires:	lxde-icon-theme
Requires:	mandriva-lxde-config >= 0.5
Conflicts:	mandriva-lxde-config-Free < 0.5
Conflicts:      mandriva-lxde-config-Flash < 0.5
Conflicts:      mandriva-lxde-config-One < 0.5
Conflicts:	mandriva-lxde-config-Powerpack < 0.5
Requires(post):	mandriva-theme

%description
This package provides a set of default configuration for LXDE.

%prep
%setup -q
%patch101 -p0 -b .pcmanfm_conf
%patch102 -p0 -b .mdv-mcc
%patch103 -p1 -b .mdv-panel
%patch106 -p0 -b .autostart
%patch109 -p0 -b .config

%build
#./autogen.sh
%configure2_5x --enable-man
%make

%install
%makeinstall_std

mkdir -p %buildroot%{_datadir}/icons
cp -f %SOURCE1 %{buildroot}%{_datadir}/icons/

#{find_lang} %{name}

# we'll ship these files via mandriva-lxde-config
rm -f %buildroot%{_sysconfdir}/xdg/lxsession/LXDE/desktop.conf %buildroot%{_datadir}/lxde/openbox/rc.xml

# we do not need this file
rm -f %buildroot%{_datadir}/xsessions/LXDE.desktop

# instead, we use wmsession.d
install -d %buildroot%_sysconfdir/X11/wmsession.d/
cat > %buildroot%_sysconfdir/X11/wmsession.d/04LXDE << EOF
NAME=LXDE
DESC=Lightweight X11 Desktops Environment
EXEC=/usr/bin/startlxde
SCRIPT:
exec /usr/bin/startlxde
EOF

# install this one manually, this provides the logout button on lxpanel:
install -m644 -D lxde-logout.desktop.in %buildroot%_datadir/applications/lxde-logout.desktop

# These macros are empty now, comment out
# %post
# %make_session

# %postun
# %make_session

%files
%config %{_sysconfdir}/xdg/lxsession/LXDE/autostart
%config %{_sysconfdir}/xdg/pcmanfm/LXDE/pcmanfm.conf
%{_sysconfdir}/X11/wmsession.d/04LXDE
%{_bindir}/*
%{_datadir}/applications/lxde-logout.desktop
%{_datadir}/lxde
%{_datadir}/lxpanel
%{_mandir}/man1/*
%{_datadir}/icons/rosa-button-lxde.png


%changelog
* Mon Jun 04 2012 akdengi <akdengi> 1:0.5.5-0.git20110808.12
- add lxde-control-center to lxpanel
- change button name to ROSA
- add logout button with user icon to lxpanel (use Button plugin)

* Mon Aug 08 2011 Александр Казанцев <kazancas@mandriva.org> 1:0.5.5-0.git20110808.2mdv2011.0
+ Revision: 693673
- revert to correct version numbering due unavalible 0.5.5.1 version
- add Droid font in pcmanfm conf
- fix pcmanfm conf file skel path
- update to minor version. Drop patches

* Sun Jul 03 2011 Александр Казанцев <kazancas@mandriva.org> 0.5.5-0.git20110721.10
+ Revision: 688608
- fix mandriva button picture

* Sat Jul 02 2011 Александр Казанцев <kazancas@mandriva.org> 0.5.5-0.git20110721.9
+ Revision: 688579
- add new mandriva button

* Sat Jun 25 2011 Александр Казанцев <kazancas@mandriva.org> 0.5.5-0.git20110721.8
+ Revision: 687081
- revert changes for lxpanel suggests

* Sat Jun 18 2011 Александр Казанцев <kazancas@mandriva.org> 0.5.5-0.git20110721.7
+ Revision: 685956
- fix spec for adding lxpanel fork dependences

* Mon Jun 13 2011 Александр Казанцев <kazancas@mandriva.org> 0.5.5-0.git20110721.6
+ Revision: 684556
- sync pcmanfm conf

* Mon Jun 13 2011 Александр Казанцев <kazancas@mandriva.org> 0.5.5-0.git20110721.5
+ Revision: 684427
- add search tools catfish
- change lxpanel customizations

* Wed May 04 2011 Александр Казанцев <kazancas@mandriva.org> 0.5.5-0.git20110721.4
+ Revision: 665859
- fix startlxde and pcmanfm config files
- add patch for missing man sources

* Sun May 01 2011 Funda Wang <fwang@mandriva.org> 0.5.5-0.git20110721.3
+ Revision: 661329
- move openbox-rc into config file

* Fri Apr 29 2011 Александр Казанцев <kazancas@mandriva.org> 0.5.5-0.git20110721.2
+ Revision: 660764
-add in autostart nm-applet, parcellite and fix keyboard TERMINATE error

* Sat Jul 24 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.5.5-0.git20110721.1mdv2011.0
+ Revision: 557358
- add missing BR
- update to 5.5 latest git to make it work with new pcmanfm2, there's no upstream
  tarball yet so go with latest git (shouldn't break stuff)
- rediff patches 101,102,103
- drop patch104, fixed upstream
- add patch105 to fix wrong file name in make file
- disable smproxy requires
- require pcmanfm >= 0.9.7
- compile with --enable-man to create openbox-lxde man page

* Thu Jun 10 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.5.0-5mdv2010.1
+ Revision: 547838
- install lxde-logout.desktop as it provides the logout icon on lxpanel

* Wed Jun 09 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.5.0-4mdv2010.1
+ Revision: 547321
- make sure autostart file gets updated to avoid upgrade problems, should
  hopefully fix (mdv #59624)

* Thu Jan 28 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.5.0-3mdv2010.1
+ Revision: 497489
- remove setxkbmap hack. The kb layout switcher works correctly with GDM;
  we shouldn't provide a hack for an incompatible dm (KDM)

* Tue Jan 26 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.5.0-2mdv2010.1
+ Revision: 496746
- add patch to make the kb layout switcher work properly
  (will be reported upstream to see about fixing it properly)
- remove requires on lxde-settings-daemon it's been
  merged in lxsession upstream some time ago
- add patch to fix startlxde script (bug 57251)
  and it's mentioned on upstream ML

* Fri Dec 11 2009 Funda Wang <fwang@mandriva.org> 0.5.0-1mdv2010.1
+ Revision: 476250
- build noarch
- use new config file location
- new version 0.5.0

* Fri Oct 02 2009 Antoine Ginies <aginies@mandriva.com> 0.4.2-3mdv2010.0
+ Revision: 452502
- xscreensaver is now a suggests to free some more space on dual CD

* Sun Sep 27 2009 Funda Wang <fwang@mandriva.org> 0.4.2-2mdv2010.0
+ Revision: 449694
- use mandriva star

* Mon Jul 06 2009 Funda Wang <fwang@mandriva.org> 0.4.2-1mdv2010.0
+ Revision: 392827
- fix file list
- new version 0.4.2

* Tue May 26 2009 Funda Wang <fwang@mandriva.org> 0.4.1-2mdv2010.0
+ Revision: 379766
- requires lxsession as there is only one available alternatives

* Thu May 07 2009 Funda Wang <fwang@mandriva.org> 0.4.1-1mdv2010.0
+ Revision: 372816
- New version 0.4.1

* Fri May 01 2009 Funda Wang <fwang@mandriva.org> 0.4-2mdv2010.0
+ Revision: 369384
- Requires lxde-settings-daemon

* Fri May 01 2009 Funda Wang <fwang@mandriva.org> 0.4-1mdv2010.0
+ Revision: 369351
- New version 0.4

* Mon Apr 06 2009 Funda Wang <fwang@mandriva.org> 0.3.2.1-17mdv2009.1
+ Revision: 364429
- promo lxterminal over xterm

* Tue Mar 10 2009 Frederic Crozat <fcrozat@mandriva.com> 0.3.2.1-16mdv2009.1
+ Revision: 353443
- Fix typo in patch0 and remove hacks in post script for background

* Mon Mar 09 2009 Frederic Crozat <fcrozat@mandriva.com> 0.3.2.1-15mdv2009.1
+ Revision: 353111
- Bump weight in wmsession.d
- Update patch0, fix mdv bug #44061

* Tue Jan 20 2009 Anne Nicolas <ennael@mandriva.org> 0.3.2.1-14mdv2009.1
+ Revision: 331830
- decrease order to avoid openbox being launched instead of LXDE by default

* Tue Nov 04 2008 Funda Wang <fwang@mandriva.org> 0.3.2.1-13mdv2009.1
+ Revision: 299957
- detect wallpaper rather than harcode file type

* Mon Sep 22 2008 Funda Wang <fwang@mandriva.org> 0.3.2.1-12mdv2009.0
+ Revision: 286429
- fix firefox button

* Thu Jul 10 2008 Pixel <pixel@mandriva.com> 0.3.2.1-11mdv2009.0
+ Revision: 233475
- remove filetrigger for gtk icon cache since %%update_icon_cache is better
  suited for a theme which comes from only one package. and %%update_icon_cache
  has been fixed

* Sun Jun 29 2008 Funda Wang <fwang@mandriva.org> 0.3.2.1-10mdv2009.0
+ Revision: 230024
- add rpm file trigger

* Sun Jun 29 2008 Funda Wang <fwang@mandriva.org> 0.3.2.1-9mdv2009.0
+ Revision: 229933
- Use lxde native terminal: lxterminal

* Tue Jun 10 2008 Funda Wang <fwang@mandriva.org> 0.3.2.1-8mdv2009.0
+ Revision: 217332
- requires virtual package lxde-session-manager

* Mon Jun 09 2008 Funda Wang <fwang@mandriva.org> 0.3.2.1-7mdv2009.0
+ Revision: 217107
- prefer lxsession-lite

* Sat May 10 2008 Funda Wang <fwang@mandriva.org> 0.3.2.1-6mdv2009.0
+ Revision: 205379
- introduce mandriva-lxde-config

* Sun May 04 2008 Funda Wang <fwang@mandriva.org> 0.3.2.1-5mdv2009.0
+ Revision: 201125
- add panel customization

* Sun May 04 2008 Funda Wang <fwang@mandriva.org> 0.3.2.1-4mdv2009.0
+ Revision: 200982
- Add mandriva customization patches
- lower BR, we only need glib and x11, not gtk

* Sun May 04 2008 Funda Wang <fwang@mandriva.org> 0.3.2.1-3mdv2009.0
+ Revision: 200917
- requries lxsession

* Sun May 04 2008 Funda Wang <fwang@mandriva.org> 0.3.2.1-2mdv2009.0
+ Revision: 200895
- Requires specific icon theme
- import source and spec
- Created package structure for lxde-common.


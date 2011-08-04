%define git git20110721

Summary:	A set of default configuration for LXDE
Name:	  	lxde-common
Version:	0.5.5.1
Release:	%mkrel 4
License:	GPLv2+
Group:		Graphical desktop/Other
Source0: 	http://dfn.dl.sourceforge.net/sourceforge/lxde/%name-%version.tar.gz
Source1:	mandriva-button-lxde.png
# Mandriva customization patch
Patch101:	lxde-common-0.5.5-pcmanfm.conf.patch
Patch102:	lxde-common-0.5.5-add-mcc-to-panel.patch
Patch103:	lxde-common-0.5.5-lxpanel-customization.patch
#Patch105:	lxde-common-0.5.5-fix-makefile.patch
Patch106:	lxde-common-0.5.5-autostart.patch
#Patch107:	lxde-common-0.5.5-openbox-lxde-man.patch
Patch109:	lxde-common-0.5.5-config.patch
#Patch110:	lxde-common-0.5.5-startlxde.patch

URL:		http://lxde.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	xsltproc docbook-style-xsl
BuildArch:	noarch
#Requires:	smproxy
Suggests:	xscreensaver
Requires:	openbox
Requires:	lxpanel
Requires:	lxsession >= 0.4.1
Requires:	pcmanfm >= 0.9.7
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
%patch103 -p0 -b .mdv-panel
#patch105 -p0 -b .makefile
%patch106 -p0 -b .autostart
#patch107 -p0 -b .man
%patch109 -p0 -b .config
#patch110 -p0 -b .startlxde

%build
#./autogen.sh
%configure2_5x --enable-man
%make

%install
rm -rf %{buildroot}
%makeinstall_std

mkdir -p %buildroot%{_datadir}/icons
cp -f %SOURCE1 %{buildroot}%{_datadir}/icons/

%{find_lang} %{name}

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

%clean
rm -rf %{buildroot}

%post
%make_session

%postun
%make_session

%files -f %{name}.lang
%defattr(-, root, root)
%config %{_sysconfdir}/xdg/lxsession/LXDE/autostart
%config %{_sysconfdir}/xdg/pcmanfm/LXDE/pcmanfm.conf
%{_sysconfdir}/X11/wmsession.d/04LXDE
%{_bindir}/*
%{_datadir}/applications/lxde-logout.desktop
%{_datadir}/lxde
%{_datadir}/lxpanel
%{_mandir}/man1/*
%{_datadir}/icons/mandriva-button-lxde.png

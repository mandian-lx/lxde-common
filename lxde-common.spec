Summary:	A set of default configuration for LXDE
Name:	  	lxde-common
Version:	0.4.1
Release:	%mkrel 2
License:	GPLv2+
Group:		Graphical desktop/Other
Source0: 	http://dfn.dl.sourceforge.net/sourceforge/lxde/%name-%version.tar.bz2
# Mandriva customization patch
Patch101:	lxde-common-0.3.2.1-use-mandriva-backgrounds.patch
Patch102:	lxde-common-0.3.2.1-add-mcc-to-panel.patch
Patch103:	lxde-common-0.4-lxpanel-customization.patch
URL:		http://lxde.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	glib2-devel libx11-devel
Requires:	smproxy
Requires:	xscreensaver
Requires:	openbox
Requires:	lxpanel
Requires:	lxsession >= 0.3.8
Requires:	pcmanfm
Requires:	nuoveXT2-icon-theme
Requires:	lxde-settings-daemon >= 0.4
Requires(post):	mandriva-theme
Requires:	lxterminal

%description
This package provides a set of default configuration for LXDE.

%package -n nuoveXT2-icon-theme
Summary:	nuoveXT2 icon theme
Group:		Graphical desktop/Other

%description -n nuoveXT2-icon-theme
This package contains nuoveXT2 icon theme for LXDE.

%prep
%setup -q
%patch101 -p1 -b .mdv-background
%patch102 -p0 -b .mdv-mcc
%patch103 -p0 -b .mdv-panel

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%{find_lang} %{name}

# we'll ship this file via mandriva-lxde-config
rm -f %buildroot%{_datadir}/lxde/config

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

touch %buildroot%{_iconsdir}/nuoveXT2/icon-theme.cache

%clean
rm -rf $RPM_BUILD_ROOT

%post
%make_session

%postun
%make_session

%post -n nuoveXT2-icon-theme
%update_icon_cache nuoveXT2

%postun -n nuoveXT2-icon-theme
%clean_icon_cache nuoveXT2

%files -f %{name}.lang
%defattr(-, root, root)
%config(noreplace) %{_sysconfdir}/xdg/lxsession/LXDE/autostart
%config(noreplace) %{_sysconfdir}/xdg/lxsession/LXDE/config
%config(noreplace) %{_sysconfdir}/xdg/lxsession/LXDE/default
%{_sysconfdir}/X11/wmsession.d/04LXDE
%{_bindir}/*
%{_datadir}/lxde
%{_datadir}/lxpanel
%{_mandir}/man1/*

%files -n nuoveXT2-icon-theme
%defattr(-, root, root)
%{_iconsdir}/nuoveXT2
%ghost %{_iconsdir}/nuoveXT2/icon-theme.cache

%define		libfm	1.0.1
Summary:	File manager for GTK
Summary(pl.UTF-8):	Zarządca plików dla GTK
Name:		pcmanfm
Version:	1.1.0
Release:	2
License:	GPL v2+
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/pcmanfm/%{name}-%{version}.tar.gz
# Source0-md5:	af0cff78690e658f3c06ceabf27bc71a
Patch0:		mate-desktop.patch
URL:		http://pcmanfm.sourceforge.net/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.31
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel
BuildRequires:	gtk+2-devel >= 2:2.8
BuildRequires:	intltool
BuildRequires:	libfm-devel >= %{libfm}
BuildRequires:	libtool
BuildRequires:	menu-cache-devel >= 0.3.2
BuildRequires:	pango-devel >= 1.20.0
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	shared-mime-info
Requires:	libfm >= %{libfm}
Suggests:	gnome-icon-theme
Suggests:	lxde-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pcmanfm is a fast and lightweight file manager which features tabbed
browsing and user-friendly interface.

%description -l pl.UTF-8
pcmanfm jest szybkim i lekkim zarządcą plików z przyjaznym interfejsem
użytkownika, umożliwiającym przeglądanie katalogów w zakładkach.

%prep
%setup -q
%patch0 -p1

%{__sed} -i -e '
	s/AM_PROG_CC_STDC/AC_PROG_CC/
' configure.ac

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-gtk=2
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# see lxde-common
install -d $RPM_BUILD_ROOT/etc/xdg/pcmanfm/LXDE

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/tt_RU

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database

%postun
%update_desktop_database

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS TODO
%dir /etc/xdg/pcmanfm
%dir /etc/xdg/pcmanfm/default
%dir /etc/xdg/pcmanfm/LXDE
%config(noreplace) %verify(not md5 mtime size) /etc/xdg/pcmanfm/default/pcmanfm.conf
%attr(755,root,root) %{_bindir}/pcmanfm
%{_mandir}/man1/pcmanfm.1*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/ui
%{_desktopdir}/pcmanfm.desktop
%{_desktopdir}/pcmanfm-desktop-pref.desktop

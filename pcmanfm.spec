#
# Conditional build:
%bcond_without	gtk3	# use GTK+ 3.x instead of GTK+ 2.x

%define		libfm_ver	1.3.2
Summary:	File manager for GTK
Summary(pl.UTF-8):	Zarządca plików dla GTK
Name:		pcmanfm
Version:	1.3.2
Release:	5
License:	GPL v2+
Group:		X11/Applications
Source0:	https://downloads.sourceforge.net/pcmanfm/%{name}-%{version}.tar.xz
# Source0-md5:	ef7c4417d2697ef138d175db7aeae15a
Patch0:		pcmanfm-1.3.2-c99.patch
URL:		http://pcmanfm.sourceforge.net/
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.31
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.18.0
%{!?with_gtk3:BuildRequires:	gtk+2-devel >= 2:2.8}
%{?with_gtk3:BuildRequires:	gtk+3-devel >= 3.0}
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libfm-devel >= %{libfm_ver}
BuildRequires:	libfm-gtk-devel >= %{libfm_ver}
BuildRequires:	libtool
BuildRequires:	menu-cache-devel >= 0.3.2
BuildRequires:	pango-devel >= 1:1.20.0
BuildRequires:	pkgconfig
%if %{with gtk3}
BuildRequires:	pkgconfig(libfm-gtk3) >= %{libfm_ver}
%else
BuildRequires:	pkgconfig(libfm-gtk) >= %{libfm_ver}
%endif
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	shared-mime-info
Requires:	glib2 >= 1:2.18.0
Requires:	libfm >= %{libfm_ver}
Requires:	pango >= 1:1.20.0
Suggests:	gnome-icon-theme
Suggests:	lxde-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pcmanfm is a fast and lightweight file manager which features tabbed
browsing and user-friendly interface.

%description -l pl.UTF-8
pcmanfm jest szybkim i lekkim zarządcą plików z przyjaznym interfejsem
użytkownika, umożliwiającym przeglądanie katalogów w zakładkach.

%package devel
Summary:	Header file for pcmanfm modules
Summary(pl.UTF-8):	Plik nagłówkowy dla modułów pcmanfm
Group:		Development/Libraries
Requires:	libfm-devel >= %{libfm_ver}

%description devel
Header file for pcmanfm modules.

%description devel -l pl.UTF-8
Plik nagłówkowy dla modułów pcmanfm.

%prep
%setup -q
%patch -P0 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_gtk3:--with-gtk=3}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# see lxde-common
install -d $RPM_BUILD_ROOT/etc/xdg/pcmanfm/LXDE
# for modules (PACKAGE_MODULES_DIR)
install -d $RPM_BUILD_ROOT%{_libdir}/pcmanfm

%{__mv} $RPM_BUILD_ROOT%{_localedir}/{tt_RU,tt}


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
%dir %{_libdir}/pcmanfm
%{_mandir}/man1/pcmanfm.1*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/ui
%{_desktopdir}/pcmanfm.desktop
%{_desktopdir}/pcmanfm-desktop-pref.desktop

%files devel
%defattr(644,root,root,755)
%{_includedir}/pcmanfm-modules.h

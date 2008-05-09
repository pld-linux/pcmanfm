Summary:	File manager for GTK
Summary(pl.UTF-8):	Zarządca plików dla GTK
Name:		pcmanfm
Version:	0.4.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/pcmanfm/%{name}-%{version}.tar.gz
# Source0-md5:	d4a528e37605df0806b5f1bd94d85604
URL:		http://pcmanfm.sourceforge.net/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	dbus-glib-devel
BuildRequires:	fam-devel
BuildRequires:	gtk+2-devel >= 2:2.8
BuildRequires:	hal-devel
BuildRequires:	libselinux-devel
BuildRequires:	pkgconfig
BuildRequires:	startup-notification-devel
Requires:	gnome-icon-theme
Requires:	shared-mime-info
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pcmanfm is a fast and lightweight file manager which features tabbed
browsing and user-friendly interface.

%description -l pl.UTF-8
pcmanfm jest szybkim i lekkim zarządcą plików z przyjaznym interfejsem
użytkownika, umożliwiającym przeglądanie katalogów w zakładkach.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -a %{name}.desktop $RPM_BUILD_ROOT%{_desktopdir}
mv $RPM_BUILD_ROOT%{_datadir}/locale/pt{_PT,}

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS TODO
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.rules
%{_datadir}/%{name}/icons
%{_datadir}/%{name}/ui
%{_datadir}/mime/packages/libmimetype.xml
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png

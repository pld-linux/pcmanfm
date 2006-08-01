Summary:	File manager for GTK
Summary(pl):	Zarz±dca plików dla GTK
Name:		pcmanfm
Version:	0.2.4
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/pcmanfm/%{name}-%{version}.tar.gz
# Source0-md5:	2362e52eec162d508955174ff7aefa0a
URL:		http://pcmanfm.sourceforge.net/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	fam-devel
BuildRequires:	gtk+2-devel >= 2:2.8
BuildRequires:	pkgconfig
Requires:	gnome-icon-theme
Requires:	shared-mime-info
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pcmanfm is a fast and lightweight file manager which features tabbed
browsing and user-friendly interface.

%description -l pl
pcmanfm jest szybkim i lekkim zarz±dc± plików z przyjaznym interfejsem
u¿ytkownika, umo¿liwiaj±cym przegl±danie katalogów w zak³adkach.

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

install %{name}.desktop $RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/%{name}.desktop

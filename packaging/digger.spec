Name:           digger
Version:        2.4.0
Release:        %autorelease
Summary:        Digger - Advanced DNS Lookup Tool

License:        GPL-3.0-or-later
URL:            https://github.com/tobagin/digger
Source0:        %{url}/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  vala
BuildRequires:  meson
BuildRequires:  blueprint-compiler
BuildRequires:  pkgconfig(gtk4) >= 4.6.0
BuildRequires:  pkgconfig(libadwaita-1) >= 1.0
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  libappstream-glib

Requires:       hicolor-icons-theme
Requires:       glib2
Requires:       %{_bindir}/dig

%description
A powerful and modern DNS lookup tool built with Vala, GTK4, and libadwaita.
Digger provides an intuitive interface for performing DNS queries with
advanced features including batch lookups, server comparison, DNSSEC validation,
and DNS-over-HTTPS support.

%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml


%files
%license LICENSE
%doc README.md
%{_bindir}/digger-vala
%{_datadir}/applications/io.github.tobagin.digger.desktop
%{_datadir}/%{name}/
%{_datadir}/glib-2.0/schemas/io.github.tobagin.digger.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/io.github.tobagin.digger*.svg
%{_metainfodir}/io.github.tobagin.digger.metainfo.xml


%changelog
%autochangelog

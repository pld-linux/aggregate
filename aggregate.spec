Summary:	Aggregate list of prefixes
Summary(pl.UTF-8):	Agregacja listy adresów
Name:		aggregate
Version:	1.6
Release:	3
License:	BSD-like
Group:		Applications/Networking
Source0:	ftp://ftp.isc.org/isc/aggregate/%{name}-%{version}.tar.gz
# Source0-md5:	6fcc515388bf2c5b0c8f9f733bfee7e1
Patch0:		optflags.patch
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
aggregate takes a list of prefixes in conventional format on stdin,
and performs two optimisations to reduce the length of the prefix
list. It removes any supplied prefixes which are supurfluous because
they are already included in another supplied prefix (e.g.,
203.97.2.0/24 would be removed if 203.97.0.0/17 was also supplied),
and identifies adjacent prefixes that can be combined under a single,
shorter-length prefix (e.g., 203.97.2.0/24 and 203.97.3.0/24 can be
combined into the single prefix 203.97.2.0/23).

%description -l pl.UTF-8
aggregate pobiera ze standardowego wejścia listę adresów sieci w
tradycyjnej postaci i wykonuje dwie optymalizacje aby zmniejszyć jej
długość. Usuwa wszelkie adresy sieci zawierające się w innych adresach
(np. 203.97.2.0/24 będzie usunięte jeżeli jest podana także
203.97.0.0/17), oraz rozpoznaje przystające adresy sieci, które mogą
być połączone w jeden, krótszy adres (np. 203.97.2.0/24 i
203.97.3.0/24 będą połączone w pojedynczy adres 203.97.2.0/23).

%prep
%setup -q
%patch -P0 -p1

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install aggregate aggregate-ios $RPM_BUILD_ROOT%{_bindir}
install aggregate.1 aggregate-ios.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE HISTORY
%attr(755,root,root) %{_bindir}/aggregate*
%{_mandir}/man1/aggregate*.1*

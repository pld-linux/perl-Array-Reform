%include	/usr/lib/rpm/macros.perl
%define	pdir	Array
%define	pnam	Reform
Summary:	Array::Reform -- Convert an array into N-sized array of arrays.
Summary(pl):	Array::Reform -- Przekonwertuj tablicê w N-d³ugo¶ci tablicê tablic.
Name:		perl-Array-Reform
Version:	1.02
Release:	1
License:	?
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ever had a list of things you needed to neetly format into a set of HTML
table rows?  Well, look no further my friend.  For the low, low price of
0.00 you too can reform you data into a neet set of lists and produce
tables from it.

%description -l pl
Ten modu³ pomo¿e Ci przekonwertowaæ tablicê w N-d³ugo¶ci tablicê tablic.
Przydatny m.in. przy umieszczaniu danych w tabeli HTML.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}
#%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/Array/Reform.pm
%{_mandir}/man3/*

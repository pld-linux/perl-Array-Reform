#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Array
%define		pnam	Reform
Summary:	Array::Reform - convert an array into N-sized array of arrays
Summary(pl):	Array::Reform - konwersja tablicy do tablicy tablic o rozmiarze N
Name:		perl-Array-Reform
Version:	1.03
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	aa7f8e776623a014db6c19a906cca409
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.005
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ever had a list of things you needed to neetly format into a set of
HTML table rows?  Well, look no further my friend.  For the low, low
price of 0.00 you too can reform you data into a neet set of lists and
produce tables from it.

%description -l pl
Ten modu³ pomaga przekszta³ciæ tablicê w tablicê tablic o rozmiarze N.
Jest przydatny m.in. przy umieszczaniu danych w tabeli HTML.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Array/Reform.pm
%dir %{perl_vendorlib}/auto/Array/Reform
%{perl_vendorlib}/auto/Array/Reform/autosplit.ix
%{_mandir}/man3/*

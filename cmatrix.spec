Summary:	CMatrix - show a scrolling 'Matrix' like screen in Linux (curses based)
Summary(pl):	CMatrix - pokazuje efekt spadaj�cych znak�w znany z filmu "Matrix"
Name:		cmatrix
Version:	1.2a
Release:	6
License:	GPL v2
Group:		Applications/Terminal
Source0:	http://www.asty.org/cmatrix/dist/%{name}-%{version}.tar.gz
# Source0-md5:	ebfb5733104a258173a9ccf2669968a1
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-setfont-consolechars-choice.patch
URL:		http://www.asty.org/cmatrix/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ncurses-devel >= 5.0
Requires(post,postun):	/usr/bin/mkfontdir
Requires:	kbd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
What is CMatrix? :-)

CMatrix is a program I wrote one evening because I didn't want to have
to run Wind*ws to see the cool scrolling lines from 'The Matrix', my
fave movie. If you haven't seen this movie and you are a fan of
computers or sci-fi in general, go see this movie!!!

%description -l pl
What is CMatrix? :-)

CMatrix zosta� napisany w jeden wiecz�r by� nie musia� uruchamia� M$
Wind*ws, aby zobaczy� na konsoli interesuj�c efekt spadaj�cych znak�w
znany z filmu "Matrix". Je�eli nie widzia�e� tego filmu, a jeste�
fanem komputer�w i sci-fi w og�lno�ci - biegnij zobaczy� ten film!!

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
CFLAGS="%{rpmcflags} -I/usr/include/ncurses"
%configure \
	--with-setfont
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/{consolefonts,fonts/misc},%{_bindir}} \
	$RPM_BUILD_ROOT%{_mandir}/man1

install cmatrix $RPM_BUILD_ROOT%{_bindir}
install cmatrix.1 $RPM_BUILD_ROOT%{_mandir}/man1
install mtx.pcf $RPM_BUILD_ROOT%{_datadir}/fonts/misc
install matrix.psf.gz $RPM_BUILD_ROOT%{_datadir}/consolefonts

gzip -9nf $RPM_BUILD_ROOT%{_datadir}/fonts/misc/*

%clean
rm -rf $RPM_BUILD_ROOT

%post
cd %{_datadir}/fonts/misc
/usr/bin/mkfontdir

%postun
cd %{_datadir}/fonts/misc
/usr/bin/mkfontdir

%files
%defattr(644,root,root,755)
%doc NEWS README TODO ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_datadir}/fonts/misc/*
%{_datadir}/consolefonts/*
%{_mandir}/man1/*

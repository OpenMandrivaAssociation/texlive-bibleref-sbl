%global tl_name bibleref-sbl
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	SBL style for the bibleref and bibleref-parse packages
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bibleref-sbl
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bibleref-sbl.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bibleref-sbl.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bibleref-sbl.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package extends the bibleref and bibleref-parse packages to support
Bible book names as specified by the Society of Biblical Literature.
This includes adjustment of abbreviations, addition of extra
Deuterocanonical books, an interface for acceptable options and correct
index sorting.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/bibleref-sbl
%dir %{_datadir}/texmf-dist/source/latex/bibleref-sbl
%dir %{_datadir}/texmf-dist/tex/latex/bibleref-sbl
%doc %{_datadir}/texmf-dist/doc/latex/bibleref-sbl/README.md
%doc %{_datadir}/texmf-dist/doc/latex/bibleref-sbl/bibleref-sbl.pdf
%doc %{_datadir}/texmf-dist/source/latex/bibleref-sbl/bibleref-sbl.dtx
%doc %{_datadir}/texmf-dist/source/latex/bibleref-sbl/bibleref-sbl.ins
%{_datadir}/texmf-dist/tex/latex/bibleref-sbl/bibleref-sbl.sty

%undefine _debugsource_packages

Name:           fzf
Version:        0.60.0
Release:        1
Summary:        A command-line fuzzy finder 
License:        MIT
URL:            https://github.com/junegunn/fzf/
Source0:        https://github.com/junegunn/fzf/archive/v%{version}/%{name}-%{version}.tar.gz
# Generated by running, inside the source tree:
# export GOPATH=$(pwd)/.godeps
# go mod download
# tar cJf ../../godeps-for-fzf-0.60.0.tar.xz .godeps
Source1:        godeps-for-fzf-%{version}.tar.xz
BuildRequires:  golang
BuildRequires:  compiler(go-compiler)

%description
It's an interactive filter program for any kind of list; files, command history, processes, hostnames, bookmarks, git commits, etc. 
It implements a "fuzzy" matching algorithm, so you can quickly type in patterns with omitted characters and still get the results you want.
Highlights

    📦 Portable — Distributed as a single binary for easy installation
    ⚡ Blazingly fast — Highly optimized code instantly processes millions of items
    🛠️ Extremely versatile — Fully customizable via an event-action binding mechanism
    🔋 Batteries included — Includes integration with bash, zsh, fish, Vim, and Neovim

%prep
%autosetup -p1 -a1

%build
export GOPATH=$(pwd)/.godeps:$(pwd)/gopath
## Note build takes around 10 minutes, so be patient as there is no output!
go build -o bin/%name

%install
export GOPATH=$(pwd)/.godeps:$(pwd)/gopath

#install -d -m 0755 %{buildroot}%{_bindir} %{buildroot}%{_datadir}/%{name}
#install -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
#install -m 0644 config/style.css %{buildroot}%{_datadir}/%{name}/style.css
install -Dpm0755 -t %{buildroot}%{_bindir} bin/fzf 
install -Dpm0755 -t %{buildroot}%{_bindir} bin/fzf-tmux

#install main binary
#install -Dpm0755 bin/%name %{buildroot}%{_bindir}/

#install tmux support
#install -Dpm0755 bin/%name-tmux %{buildroot}%{_bindir}/

install -Dpm0644 -t %{buildroot}%{_mandir}/man1 man/man1/*.1

# Install vim plugin
install -Dpm0644 -t %{buildroot}%{_datadir}/vim/vimfiles/plugin plugin/fzf.vim
install -Dpm0644 -t %{buildroot}%{_datadir}/nvim/site/plugin plugin/fzf.vim

# Install shell completion
# fzf is special, bash completion must be in /etc/bash_completion.d
# https://bugzilla.redhat.com/show_bug.cgi?id=1789958#c7
install -Dpm0644 shell/completion.bash %{buildroot}%{_sysconfdir}/bash_completion.d/fzf
install -Dpm0644 shell/completion.zsh %{buildroot}%{zsh_completions_dir}/_fzf

# Install shell key bindings (not enabled)
install -Dpm0644 -t %{buildroot}%{_datadir}/fzf/shell shell/key-bindings.*

%files
%license LICENSE
%{_bindir}/fzf
%{_bindir}/fzf-tmux
%{_mandir}/man1/fzf.1*
%{_mandir}/man1/fzf-tmux.1*
%{_datadir}/fzf
%dir %{_datadir}/vim/vimfiles/plugin
%{_datadir}/vim/vimfiles/plugin/fzf.vim
%dir %{_datadir}/nvim/site/plugin
%{_datadir}/nvim/site/plugin/fzf.vim
%{_sysconfdir}/bash_completion.d/fzf
#{zsh_completions_dir}/_fzf

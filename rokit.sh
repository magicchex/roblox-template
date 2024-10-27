# prompt () {
# printf "$1"
# read -p "$2"
# }
cargo install rokit --locked --force
tools_bool=0
while read line
do
if [[ "$line" == "[tools]" ]]; then
    tools_bool=1
fi
if (( "$tools_bool" > "0" )); then
    if [[ "$line" =~ \"([^\"]*)\" ]]; then
        rokit trust ${BASH_REMATCH[1]%@*}
    fi
fi
done < "rokit.toml"
rokit install
# prompt "Done running test\n" ""

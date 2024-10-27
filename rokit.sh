# prompt () {
# printf "$1"
# read -p "$2"
# }
# cargo install rokit
echo "Reading rokit.toml"
tools_bool=0
while read line
do
if [[ "$line" == "[tools]" ]]; then
    echo "Found rokit tools header"
    tools_bool=1
fi
if (( "$tools_bool" > "0" )); then
    if [[ "$line" =~ \"([^\"]*)\" ]]; then
        tool=${BASH_REMATCH[1]%@*}
        echo "Trusting $tool"
        rokit trust $tool
    fi
fi
done < "rokit.toml"
rokit install
# prompt "Done running test\n" ""

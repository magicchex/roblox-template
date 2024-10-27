# prompt () {
# printf "$1"
# read -p "$2"
# }
tools_bool=0

while read line
do
    echo $line
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
done < "./rokit.toml"
# prompt "Done running test\n" ""

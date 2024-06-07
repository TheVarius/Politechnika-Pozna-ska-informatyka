#!/bin/bash
space="/"
dash="-"
dot="."
morse=""


if [ $# -eq 0 ] # wyswietlenie menusow jesli nic nie zostalo podane
  then
    echo -D Parametr dla kropki
    echo -d Parametr dla myślnika
    echo -h Wyświetlenie pomocy
    echo " "
fi

if [ "${1:0:1}" != "-" ]; then # sprawdzanie czy uzytkownik dal arg z poczatkiem "-" (aby uniknac podawania inputu odrazu) 
    echo "Nie podawaj tekstu jako argumentu. Tekst należy wprowadzić po uruchomieniu programu."
    exit 1
fi

while getopts "D:d:h" arg; do # ustawienie parametrow
    case $arg in
        D)
        if [ ${#2} -eq 1 ]; then # warunek sprawdzajacy, czy znak zastepczy jest pojedynczy (length)
            dot="$OPTARG"
        else
        echo Możesz wstawić tylko jeden znak w zamian za znak domyślny.
        exit 1
        fi
            ;;
        d)
        if [ ${#2} -eq 1 ]; then # warunek sprawdzajacy, czy znak zastepczy jest pojedynczy (length)
            dash="$OPTARG"
        else
        echo Możesz wstawić tylko jeden znak w zamian za znak domyślny.
        exit 1
        fi
            ;;
        h)
            echo -D Parametr dla kropki
            echo -d Parametr dla myślnika
            echo -h Wyświetlenie pomocy
            exit 0
            ;;
        *)
            exit 1
            ;;
    esac
done

declare -A alphabet_to_morse=(
    [A]="$dot$dash" [B]="$dash$dot$dot$dot" [C]="$dash$dot$dash$dot" [D]="$dash$dot$dot" [E]="$dot"
    [F]="$dot$dot$dash$dot" [G]="$dash$dash$dot" [H]="$dot$dot$dot$dot" [I]="$dot$dot" [J]="$dot$dash$dash$dash"
    [K]="$dash$dot$dash" [L]="$dot$dash$dot$dot" [M]="$dash$dash" [N]="$dash$dot" [O]="$dash$dash$dash"
    [P]="$dot$dash$dash$dot" [Q]="$dash$dash$dot$dash" [R]="$dot$dash$dot" [S]="$dot$dot$dot" [T]="$dash"
    [U]="$dot$dot$dash" [V]="$dot$dot$dot$dash" [W]="$dot$dash$dash" [X]="$dash$dot$dot$dash" [Y]="$dash$dot$dash$dash"
    [Z]="$dash$dash$dot$dot" [a]="$dot$dash" [b]="$dash$dot$dot$dot" [c]="$dash$dot$dash$dot" [d]="$dash$dot$dot"
    [e]="$dot" [f]="$dot$dot$dash$dot" [g]="$dash$dash$dot" [h]="$dot$dot$dot$dot" [i]="$dot$dot"
    [j]="$dot$dash$dash$dash" [k]="$dash$dot$dash" [l]="$dot$dash$dot$dot" [m]="$dash$dash" [n]="$dash$dot"
    [o]="$dash$dash$dash" [p]="$dot$dash$dash$dot" [q]="$dash$dash$dot$dash" [r]="$dot$dash$dot" [s]="$dot$dot$dot"
    [t]="$dash" [u]="$dot$dot$dash" [v]="$dot$dot$dot$dash" [w]="$dot$dash$dash" [x]="$dash$dot$dot$dash" [y]="$dash$dot$dash$dash"
    [z]="$dash$dash$dot$dot" [0]="$dash$dash$dash$dash$dash" [1]="$dot$dash$dash$dash$dash" [2]="$dot$dot$dash$dash$dash"
    [3]="$dot$dot$dot$dash$dash" [4]="$dot$dot$dot$dot$dash" [5]="$dot$dot$dot$dot$dot" [6]="$dash$dot$dot$dot$dot" [7]="$dash$dash$dot$dot$dot"
    [8]="$dash$dash$dash$dot$dot" [9]="$dash$dash$dash$dash$dot" [" "]="$space"
)

function conversion { # konwersja na morse'a
    echo "Wprowadź tekst: "
    read text
    for (( i=0; i<${#text}; i++ )); do
        char="${text:$i:1}"
        morse+="${alphabet_to_morse[$char]} "  # spacja, aby po literkach była przerwa (tak podobno się robi w kodzie morse'a)
    done
    echo "$morse"
}

function sound { # konwersja z morse'a na dzwiek
    for (( j=0; j<${#morse}; j++ )); do
        symbol="${morse:$j:1}"
        if [ "$symbol" == "$dash" ]; then
                aplay beep_dash.wav
                sleep 1.5
        elif [ "$symbol" == "$dot" ]; then
                aplay beep_dot.wav
                sleep 1.5
        elif [ "$symbol" == "$space" ]; then
                sleep 2
        fi
        done
}


conversion
sound

#https://www.geeksforgeeks.org/bash-scripting-string/
#https://stackoverflow.com/questions/10551981/how-to-perform-a-for-loop-on-each-character-in-a-string-in-bash
#https://www.linuxexpert.pl/2010/09/29/bash-pobieranie-opcji-z-linii-polecen-wersja-2-czyli-getopts/
#https://stackoverflow.com/questions/6482377/check-existence-of-input-argument-in-a-bash-shell-script
#https://unix.stackexchange.com/questions/214141/explain-the-shell-command-shift-optind-1
#https://www.geeksforgeeks.org/aplay-command-in-linux-with-examples/
#https://medium.com/@linuxschooltech/create-and-use-associative-array-in-bash-script-5f4e32a00577


#id: sop
#password: sopsop

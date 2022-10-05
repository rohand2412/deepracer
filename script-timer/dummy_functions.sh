function dr-start-evaluation {
    echo dr-start-evaluation
    echo "asfasdkljhasfjasdjfhasdjkhjfsdhajkfhasdjkfhasjhfasjkfhasdjk"
    sleep 5
    i=0
    while [[ $i -lt 5 ]]
    do
        echo "done"
        # echo $i
        ((i++))
        sleep 1
    done
    echo "... shutting down processing monitor complete"
    sleep 5
    echo "done"
}

function dr-stop-evaluation {
    echo dr-stop-evaluation
}

echo ran entire file
/** @jsxImportSource @emotion/react */
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { Paper, InputBase, Button } from "@mui/material";
import { search,searchBtn,elem,intro,toImage } from "../../css/result_csst";
import { useDispatch,useSelector, RootStateOrAny } from "react-redux";
import { setWord } from "../../redux/search";
import { useNavigate } from "react-router";

export const TextSearchBar = () => {
    const dispatch = useDispatch();
    const navigate = useNavigate();
    // const searchWord = useSelector((state:RootStateOrAny) => state.searchText.word)

    const [userText, setUserText] = useState(''); // 텍스트 검색어

    // let input = (document.getElementById('searchInput') as HTMLInputElement).value

    // useEffect(() => {
    //     console.log(input);
    // },[userText])

    const handleTextClick = () => {
        console.log('<textSearchBar> : 검색 버튼 누름, before dispatch')
        dispatch(setWord(userText))
        console.log('<textSearchBar> : 검색 버튼 누름, after dispatch')
        navigate(`/result?data=${userText}`)
        console.log('<textSearchBar> : after navigate')
    }

    const handleKeyPress = (e:any) => {
        if(e.key === 'Enter'){
            e.preventDefault();
            handleTextClick();
        }
    }

    return (
        <>
            <div>
                <p css={intro}>원하는 검색어를 입력해주세요.</p>
                <div css={elem}>
                    <Paper component="form" className="paper" css={search}>
                            <InputBase
                                id="searchInput"
                                sx={{ ml: 4, flex: 1 }}
                                placeholder="예) 김치볶음밥, 된장찌개, 닭볶음탕"
                                inputProps={{ 'aria-label': 'search google maps' }}
                                // value={userText}
                                onChange={(e) => setUserText(e.target.value)}
                                onKeyPress={handleKeyPress} 
                            />
                    </Paper>
                    <Button
                        className="searchButton"
                        css={searchBtn}
                        onClick={handleTextClick}
                    >
                        검색
                    </Button>
                </div>
                <p css={toImage}>
                    <Link to="/" style={{textDecoration:'none', color:'blue'}}>
                        이미지 검색
                    </Link>
                </p>
            </div>
        </>
    );
}

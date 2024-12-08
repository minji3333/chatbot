CSS = """
<style>
.stHorizontalBlock {
    margin-left: 60px;
}

.stColumn {
    margin: 0;
    padding: 0;
    width: auto;
    flex: none;
}

[data-testid="stVerticalBlock"] > [data-testid="stVerticalBlockBorderWrapper"] > div > [data-testid="stVerticalBlock"] > [data-testid="stHorizontalBlock"] {
    display: block;
    flex-direction: row;
    overflow-x: scroll;
    overflow-y: scroll;  /* 세로 스크롤을 숨기기 */
    white-space: nowrap; 
}

[data-testid="stVerticalBlock"] > [data-testid="stVerticalBlockBorderWrapper"] > div > [data-testid="stVerticalBlock"] > [data-testid="stHorizontalBlock"] > [data-testid="stColumn"] {
    display: inline-block;
    width: 300px;
    flex: none;
    margin-right: 1rem;
}

.stExpander img {
    object-fit: cover;
    border-radius: 8px;
}

strong {
    white-space: normal;
    word-wrap: break-word;
}
</style>
"""
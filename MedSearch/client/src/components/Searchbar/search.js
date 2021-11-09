const SearchBar = () => (
    <form action="/" method="get">
        <label htmlFor="header-search">
            <span className="visually-hidden">Search doctor</span>
        </label>
        <input
            type="text"
            id="header-search"
            placeholder="Doctor's name"
            name="s" 
        />
        <button type="submit">Search</button>
    </form>
);

export default SearchBar;
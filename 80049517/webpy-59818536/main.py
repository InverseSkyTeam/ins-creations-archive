code = """
(async () => {
    const response = await fetch(
        "https://passport.100tal.com/v1/web/login/status/check",
        {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                "Accept": "application/json",
            },
            credentials: "include",
        }
    );
    const responseData = await response.json();
    refWsTerm.fnWriteln(responseData.data.tal_token);
})();
"""
jseval(code)
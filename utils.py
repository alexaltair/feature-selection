def head(data, results, n=10):
    results['preview'] = data.iloc[:n].to_html(index=False,
        classes=['table', 'table-condensed', 'table-bordered', 'table-striped'])

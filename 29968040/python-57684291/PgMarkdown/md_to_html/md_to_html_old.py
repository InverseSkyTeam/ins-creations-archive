try:
    import pypandoc
    import re
except:
    import re


extra = [
    '-abbreviations',
    '+all_symbols_escapable',
    '-angle_brackets_escapable',
    '-autolink_bare_uris',
    '+backtick_code_blocks',
    '-blank_before_blockquote',
    '-blank_before_header'
    '-bracketed_spans',
    '-citations',
    '-compact_definition_lists',
    '-definition_lists',
    '-east_asian_line_breaks',
    '-emoji',
    '+escaped_line_breaks',
    '-example_lists',
    '-fancy_lists',
    '+fenced_code_attributes',
    '+fenced_code_blocks',
    '-fenced_divs',
    '-footnotes',
    '-four_space_rule',
    '-grid_tables',
    '-gutenberg',
    '-hard_line_breaks',
    '-header_attributes',
    '-ignore_line_breaks',
    '-implicit_figures',
    '-implicit_header_references',
    '-inline_code_attributes',
    '-inline_notes',
    '+intraword_underscores',
    '-latex_macros',
    '-line_blocks',
    '-link_attributes',
    '+lists_without_preceding_blankline',
    '-markdown_attribute',
    '-markdown_in_html_blocks',
    '-mmd_header_identifiers',
    '-mmd_link_attributes',
    '-mmd_title_block',
    '-multiline_tables',
    '-native_divs',
    '-native_spans',
    '-old_dashes',
    '-pandoc_title_block',
    '+pipe_tables',
    '-raw_attribute',
    '+raw_html',
    '-raw_tex',
    '-rebase_relative_paths',
    '-short_subsuperscripts',
    '-shortcut_reference_links',
    '-simple_tables',
    '+space_in_atx_header',
    '-spaced_reference_links',
    '+startnum',
    '+strikeout',
    '-subscript',
    '-superscript',
    '-table_captions',
    '-task_lists',
    '+tex_math_dollars',
    '-tex_math_double_backslash',
    '-tex_math_single_backslash',
    '-yaml_metadata_block'
]
pdoc_args = ['--from', 'markdown_strict'+''.join(extra), '--katex', '--no-highlight', '--columns=2147483647']


def md_to_html(md_string):
    md_string = re.sub(r'_{3,}', '\n---\n', md_string)
    output = pypandoc.convert_text(md_string, to='html5', format='md',  
                                   extra_args=pdoc_args)
    return '<html><head></head><body>'+output+'</body></html>'

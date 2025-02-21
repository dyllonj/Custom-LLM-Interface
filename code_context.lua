local plenary = require("plenary")
local job = require("plenary.job")
-- save this at ~/.config/nvim/lua/code_context.lua
-- Get current buffer content
local function get_buffer_content()
    local lines = vim.api.nvim_buf_get_lines(0, 0, -1, false)
    return table.concat(lines, "\n")
end

-- Send context to LLM via the chat script
local function send_to_llm(context)
    local cmd = "python3 /path/to/llm_chat.py \"" .. context .. "\""
    job:new({
        command = "bash",
        args = {"-c", cmd},
        on_exit = function(j, return_val)
            if return_val == 0 then
                print("LLM Response: " .. j:result()[1])
            else
                print("Error sending to LLM")
            end
        end
    }):start()
end

-- Bind to a key (e.g., <Leader>ll) to send current code to LLM
vim.api.nvim_set_keymap("n", "<Leader>ll", ":lua send_to_llm(get_buffer_content())<CR>", {noremap = true, silent = true})

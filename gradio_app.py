import gradio as gr
import requests

with gr.Blocks() as demo:
    with gr.Row():
        pdf_input = gr.File(label="Upload a PDF", file_types=[".pdf"])
        upload_btn = gr.Button("Process Document")

    output_status = gr.Textbox(label="Status", interactive=False)

    with gr.Row():
        query_input = gr.Textbox(
            label="Ask a Question",
            placeholder="e.g., What is coverage for accident?"
        )
        ask_btn = gr.Button("Get Answer")

    answer_output = gr.Textbox(label="Answer", lines=10)
    retriever_ready = gr.State(False)

    upload_btn.click(
        fn=process_doc,
        inputs=[pdf_input],
        outputs=[output_status]
    ).then(
        fn=lambda _: True,
        inputs=None,
        outputs=retriever_ready
    )

    ask_btn.click(
        fn=query_answer,
        inputs=[query_input, retriever_ready],
        outputs=[answer_output]
    )

demo.launch(share=True)

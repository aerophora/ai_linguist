from pathlib import Path

from openai import OpenAI

from ..configs.main import Config
from ..engine.create_note import create_note
from ..engine.executor import executor
from ..engine.poll import poll


def process_polling(
    openai: OpenAI, knowledge: list[Path], config: Config
) -> None:
    try:
        for result, question in poll(handler=executor, openai=openai):
            results = {
                "first": f"{result.choices[0].message.content}",
                "second": f"{result.choices[1].message.content}",
                "third": f"{result.choices[2].message.content}",
            }

            print(
                "\n3 responses received from GPT 🤖\n",
                results.get("first"),
                results.get("second"),
                results.get("third"),
                sep="\n",
            )

            t_f = create_note(
                data=results,
                question=question,
                knowledge=knowledge,
                config=config,
            )

            if t_f and not isinstance(t_f, list):
                print("\n\nSuccess! ✨\n\n")
            elif isinstance(t_f, list) and t_f[0] == "Incorrect choise":
                print(
                    f"\n\nInterrupted due to incorrect choise: "
                    f"{t_f[1]}! 🙂‍↔️\n\n"
                )
            else:
                print("\n\nInterrupted! ✨\n\n")

    except KeyboardInterrupt:
        print("\n\nBye! 👋🏻\n\n")

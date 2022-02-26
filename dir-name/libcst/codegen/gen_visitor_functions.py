# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from dataclasses import fields
from typing import List

from libcst.codegen.gather import imports, nodebases, nodeuses

generated_code: List[str] = []
generated_code.append("# Copyright (c) Meta Platforms, Inc. and affiliates.")
generated_code.append("#")
generated_code.append(
    "# This source code is licensed under the MIT license found in the"
)
generated_code.append("# LICENSE file in the root directory of this source tree.")
generated_code.append("")
generated_code.append("")
generated_code.append("# This file was generated by libcst.codegen.gen_matcher_classes")
generated_code.append("from typing import Optional, Union, TYPE_CHECKING")
generated_code.append("")
generated_code.append("from libcst._flatten_sentinel import FlattenSentinel")
generated_code.append("from libcst._maybe_sentinel import MaybeSentinel")
generated_code.append("from libcst._removal_sentinel import RemovalSentinel")
generated_code.append("from libcst._typed_visitor_base import mark_no_op")

# Import the types we use. These have to be type guarded since it would
# cause an import cycle otherwise.
generated_code.append("")
generated_code.append("")
generated_code.append("if TYPE_CHECKING:")
for module, objects in imports.items():
    generated_code.append(f"    from {module} import (  # noqa: F401")
    generated_code.append(f"        {', '.join(sorted(list(objects)))}")
    generated_code.append("    )")


# Generate the base visit_ methods
generated_code.append("")
generated_code.append("")
generated_code.append("class CSTTypedBaseFunctions:")
for node in sorted(nodebases.keys(), key=lambda node: node.__name__):
    name = node.__name__
    if name.startswith("Base"):
        continue

    generated_code.append("")
    generated_code.append("    @mark_no_op")
    generated_code.append(
        f'    def visit_{name}(self, node: "{name}") -> Optional[bool]:'
    )
    generated_code.append("        pass")
    for field in fields(node) or []:
        if field.name == "_metadata":
            continue
        generated_code.append("")
        generated_code.append("    @mark_no_op")
        generated_code.append(
            f'    def visit_{name}_{field.name}(self, node: "{name}") -> None:'
        )
        generated_code.append("        pass")
        generated_code.append("")
        generated_code.append("    @mark_no_op")
        generated_code.append(
            f'    def leave_{name}_{field.name}(self, node: "{name}") -> None:'
        )
        generated_code.append("        pass")

# Generate the visitor leave_ methods
generated_code.append("")
generated_code.append("")
generated_code.append("class CSTTypedVisitorFunctions(CSTTypedBaseFunctions):")
for node in sorted(nodebases.keys(), key=lambda node: node.__name__):
    name = node.__name__
    if name.startswith("Base"):
        continue

    generated_code.append("")
    generated_code.append("    @mark_no_op")
    generated_code.append(
        f'    def leave_{name}(self, original_node: "{name}") -> None:'
    )
    generated_code.append("        pass")

# Generate the transformer leave_ methods
generated_code.append("")
generated_code.append("")
generated_code.append("class CSTTypedTransformerFunctions(CSTTypedBaseFunctions):")
generated_code.append("    pass")
for node in sorted(nodebases.keys(), key=lambda node: node.__name__):
    name = node.__name__
    if name.startswith("Base"):
        continue
    generated_code.append("")
    generated_code.append("    @mark_no_op")
    valid_return_types: List[str] = [f'"{nodebases[node].__name__}"']
    node_uses = nodeuses[node]
    base_uses = nodeuses[nodebases[node]]
    if node_uses.maybe or base_uses.maybe:
        valid_return_types.append("MaybeSentinel")

    if node_uses.sequence or base_uses.sequence:
        valid_return_types.append(f'FlattenSentinel["{nodebases[node].__name__}"]')
        valid_return_types.append("RemovalSentinel")
    elif node_uses.optional or base_uses.optional:
        valid_return_types.append("RemovalSentinel")

    generated_code.append(
        f'    def leave_{name}(self, original_node: "{name}", updated_node: "{name}") -> Union[{", ".join(valid_return_types)}]:'
    )
    generated_code.append("        return updated_node")

if __name__ == "__main__":
    # Output the code
    print("\n".join(generated_code))
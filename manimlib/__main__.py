#!/usr/bin/env python
import pretty_errors #lcj加
import manimlib.config
import manimlib.extract_scene
import manimlib.utils.init_config


import os
import sys

def main():
    #lcj: 如果不把cwd加到path里，那从脚本所在同一个文件夹中import的模块就会找不到
    sys.path.append(os.getcwd())
    sys.path.append('c:/StarSky/VideoCrafting/MyProjects/[manim]2022-2欧拉公式/')#debug临时加
    print('hello')
	
    args = manimlib.config.parse_cli()

    if args.config:
        manimlib.utils.init_config.init_customization()
    else:
        config = manimlib.config.get_configuration(args)
        scenes = manimlib.extract_scene.main(config)

        for scene in scenes:
            scene.run()

if __name__ == '__main__':
    main()

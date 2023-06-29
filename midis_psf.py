#!/usr/bin/env  python

import os
import argparse
from astropy.io import fits
from astropy.wcs import WCS

ROOT = os.path.dirname(__file__)
PSF_MAP = os.path.join(ROOT, './data-{}/midis_psf_map.fits')
PSF_TMPL = os.path.join(ROOT, './data-{}/{}mas/HUDF_F560W_i2d-psf_inserted-original{}-cutout-bg-norm.fits')

def get_psf(ra_deg, dec_deg, filename_only=True, version='v3', pixscale=60):
    """Get MIDI PSF model for (ra,dec).

    ra_deg: float
       ra in degrees
    deg_deg: float
       deg in degrees

    """

    with fits.open(PSF_MAP.format(version)) as hdu:
        map_wcs = WCS(hdu[0].header)
        map_data = hdu[0].data

        x, y = map_wcs.all_world2pix(ra_deg, dec_deg, 0)

        try:
            # nearest pixel
            psf_idx = int(map_data[int(y), int(x)])
        except:
            psf_idx = 0

        if psf_idx == 0:
            print(f"No psf for ({ra_deg}, {dec_deg}).")
            return 0
        elif filename_only:
            print(PSF_TMPL.format(version, pixscale, psf_idx))
            return PSF_TMPL.format(version, pixscale, psf_idx)
        else:
            with fits.open(PSF_TMPL.format(version, pixscale, psf_idx)) as hdu2:
                return hdu2[0].data


def main(args=None):
    parser = argparse.ArgumentParser(description="""Get MIDI PSF model for (ra,dec).""")

    parser.add_argument("ra_deg", type=float,
                        help="ra in degrees")
    parser.add_argument("dec_deg", type=float,
                        help="dec in degrees")
    parser.add_argument('-f', '--filename_only', type=bool, default=True,
                        help="return filename only (default: true)")
    parser.add_argument('-v', '--version', type=str, default='v3',
                        help="version of psf to use (default: latest)")
    parser.add_argument('-p', '--pixscale', type=int, default=60,
                        choices=[30, 40, 60], help="pixscale in mas")

    args = parser.parse_args(args)

    return get_psf(args.ra_deg, args.dec_deg, args.filename_only, args.version, args.pixscale)


if __name__ == '__main__':
    main()
